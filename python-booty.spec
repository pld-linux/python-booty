Summary:	Simple Python bootloader config lib
Summary(pl):	Prosta biblioteka Pythona do konfiguracji bootloadera
Name:		python-booty
Version:	0.71
Release:	0.6
License:	LGPL
Group:		Libraries
Source0:	booty-%{version}.tar.bz2
# Source0-md5:	50dd1a34e60c3191d4898cef90f45319
Patch0:		%{name}-menu.lst.patch
Patch1:		%{name}-pld.patch
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.234
Requires:	python-rhpl >= 0.176-1.1
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
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS='%{rpmcflags} -fPIC -Wall -I$(PYTHONINCLUDE)' \
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
%{_libdir}/booty/bootloaderInfo.py[co]
%{_libdir}/booty/booty.py[co]
%{_libdir}/booty/butil.py[co]
%{_libdir}/booty/checkbootloader.py[co]
%{_libdir}/booty/grubupdatetest.py[co]
%{_libdir}/booty/lilo.py[co]
