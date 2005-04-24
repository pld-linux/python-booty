Summary:	Simple Python bootloader config lib
Summary(pl):	Prosta biblioteka Pythona do konfiguracji bootloadera
Name:		python-booty
Version:	0.51
Release:	1
License:	LGPL
Group:		Libraries
Source0:	booty-%{version}.tar.bz2
# Source0-md5:	eeeaad1bc27e7c67410a8b909deef150
BuildRequires:	python-devel
%pyrequires_eq	python-libs
Requires:	python-rhpl
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%dir %{_libdir}/booty
%attr(755,root,root) %{_libdir}/booty/eddmodule.so
%{_libdir}/booty/*.py[co]
