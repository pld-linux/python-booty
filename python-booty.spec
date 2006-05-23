Summary:	Simple Python bootloader config lib
Summary(pl):	Prosta biblioteka Pythona do konfiguracji bootloadera
Name:		python-booty
Version:	0.71
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	booty-%{version}.tar.bz2
# Source0-md5:	50dd1a34e60c3191d4898cef90f45319
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.234
Requires:	python-rhpl
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small Python library for use with bootloader configuration by anaconda
and up2date.

%description -l pl
Prosta biblioteka Pythona do konfiguracji bootloadera u¿ywana przez
anacondê i up2date.

%prep
%setup -q -n booty-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wall -I\$(PYTHONINCLUDE)" \
	PYTHONLIBDIR=%{_libdir}/booty

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHONLIBDIR=%{_libdir}/booty

%py_postclean %{_libdir}/booty

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%dir %{_libdir}/booty
%ifarch %{ix86}
%attr(755,root,root) %{_libdir}/booty/eddmodule.so
%endif
%{_libdir}/booty/*.py[co]
