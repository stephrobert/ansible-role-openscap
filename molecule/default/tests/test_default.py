"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_python_is_installed(host):
    distribution=host.system_info.distribution
    if distribution in ['debian','fedora','ubuntu']:
        python = host.package("python3")
    else:
        python = host.package("python")

    assert python.is_installed
