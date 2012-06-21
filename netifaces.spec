%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from %distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           python-netifaces
Version:        0.8
Release:        1%{?dist}
Summary:        Python library to retrieve information about network interfaces

Group:          Development/Libraries
License:        MIT
URL:            http://alastairs-place.net/netifaces/
Source0:        http://alastairs-place.net/2007/03/netifaces/netifaces-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel

Requires:       python

%description
This package provides a cross platform API for getting address information
from network interfaces.


%prep
%setup -q -n netifaces-%{version}


%build
python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT
chmod -x $RPM_BUILD_ROOT%{python_sitearch}/netifaces-%{version}-*.egg-info/*


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README
%{python_sitearch}/netifaces-%{version}-*.egg-info/
%{python_sitearch}/netifaces.so

%changelog
* Wed Jun 1 2011 Ryan Rix <ry@n.rix.si> 0.5-1
- Initial packaging effort
