Summary:	build essential packages
Name:		build-essential
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/File
Requires:	gcc
Requires:	glibc-devel
Requires:	make
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
