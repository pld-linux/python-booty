Summary:	Simple Python bootloader config lib
Summary(pl.UTF-8):	Prosta biblioteka Pythona do konfiguracji bootloadera
Name:		python-booty
Version:	0.93
Release:	7
License:	LGPL
Group:		Libraries
# https://fedorahosted.org/releases/b/o/booty/ (not yet)
Source0:	booty-%{version}.tar.bz2
# Source0-md5:	e0dff87df9a94378ed6a4b5291edaaf7
Patch0:		%{name}-menu.lst.patch
Patch1:		%{name}-pld.patch
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.234
Requires:	python-rhpl >= 0.176-1.1
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small Python library for use with bootloader configuration by anaconda
and up2date.

%description -l pl.UTF-8
Prosta biblioteka Pythona do konfiguracji bootloadera używana przez
anacondę i up2date.

%prep
%setup -q -n booty-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} \
	PYTHONLIBDIR=%{py_sitescriptdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHONLIBDIR=%{py_sitescriptdir}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{py_sitescriptdir}/*.py[co]
