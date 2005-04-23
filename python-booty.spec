Summary:	Simple python bootloader config lib
Name:		python-booty
Version:	0.51
Release:	1
License:	LGPL
Group:		System Environment/Libraries
Source0:	booty-%{version}.tar.bz2
# Source0-md5:	eeeaad1bc27e7c67410a8b909deef150
BuildRequires:	python-devel
Requires:	python-rhpl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small python library for use with bootloader configuration by anaconda
and up2date.

%prep
%setup -q -n booty-%{version}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{_libdir}/booty
