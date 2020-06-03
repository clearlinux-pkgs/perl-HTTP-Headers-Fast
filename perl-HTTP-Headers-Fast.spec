#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Headers-Fast
Version  : 0.22
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/HTTP-Headers-Fast-0.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/HTTP-Headers-Fast-0.22.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhttp-headers-fast-perl/libhttp-headers-fast-perl_0.21-1.debian.tar.xz
Summary  : 'faster implementation of HTTP::Headers'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Headers-Fast-license = %{version}-%{release}
Requires: perl-HTTP-Headers-Fast-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
# NAME
HTTP::Headers::Fast - faster implementation of HTTP::Headers
# SYNOPSIS
use HTTP::Headers::Fast;
# and, same as HTTP::Headers.

%package dev
Summary: dev components for the perl-HTTP-Headers-Fast package.
Group: Development
Provides: perl-HTTP-Headers-Fast-devel = %{version}-%{release}
Requires: perl-HTTP-Headers-Fast = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Headers-Fast package.


%package license
Summary: license components for the perl-HTTP-Headers-Fast package.
Group: Default

%description license
license components for the perl-HTTP-Headers-Fast package.


%package perl
Summary: perl components for the perl-HTTP-Headers-Fast package.
Group: Default
Requires: perl-HTTP-Headers-Fast = %{version}-%{release}

%description perl
perl components for the perl-HTTP-Headers-Fast package.


%prep
%setup -q -n HTTP-Headers-Fast-0.22
cd %{_builddir}
tar xf %{_sourcedir}/libhttp-headers-fast-perl_0.21-1.debian.tar.xz
cd %{_builddir}/HTTP-Headers-Fast-0.22
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTTP-Headers-Fast-0.22/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Headers-Fast
cp %{_builddir}/HTTP-Headers-Fast-0.22/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-Headers-Fast/84f960e297673c6ceec765aa4f79e0eb3763b4a0
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTTP-Headers-Fast/96423635b5647cdf510db0ff016e27244757c23f
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Headers::Fast.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Headers-Fast/84f960e297673c6ceec765aa4f79e0eb3763b4a0
/usr/share/package-licenses/perl-HTTP-Headers-Fast/96423635b5647cdf510db0ff016e27244757c23f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/HTTP/Headers/Fast.pm
