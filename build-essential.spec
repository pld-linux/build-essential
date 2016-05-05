Summary:	build essential packages
Name:		build-essential
Version:	0.1
Release:	1
License:	GPL
Group:		Development/Building
Requires:	awk
Requires:	bash
Requires:	coreutils
Requires:	diffutils
Requires:	gcc
Requires:	glibc-devel
Requires:	grep
Requires:	gzip
Requires:	hostname
Requires:	make
Requires:	patch
Requires:	sed >= 4.0
Requires:	tar >= 1:1.22
Requires:	util-linux
Requires:	which
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package depends on the packages which are considered essential
for building packages.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
