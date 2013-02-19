Summary:	AES XvBA SDK for Linux
Summary(pl.UTF-8):	SDK AES XvBA dla Linuksa
Name:		xvba-sdk
Version:	0.74
Release:	1
License:	BSD-like
Group:		Applications
Source0:	http://developer.amd.com/wordpress/media/2012/10/%{name}-%{version}-404001.tar.gz
# Source0-md5:	b8f56bc55aa70cb19dd12857fdc184cc
URL:		http://developer.amd.com/tools/open-source/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the AMD Embedded Solutions X-Video Bitstream
Acceleration software development kit for Linux.

%description -l pl.UTF-8
Ten pakiet zawiera SDK AMD Embedded Solutions (AES) X-Video Bitstream
Acceleration (XvBA) dla Linuksa.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -D include/amdxvba.h $RPM_BUILD_ROOT%{_includedir}/amdxvba.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README doc/AMD_XvBA_Spec_v0_74_01_AES_2.pdf
%{_includedir}/amdxvba.h
