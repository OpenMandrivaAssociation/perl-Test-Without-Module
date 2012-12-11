%define upstream_name    Test-Without-Module
%define upstream_version 0.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Test::Without::Module - Test fallback behaviour in absence of modules
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Inline)
BuildArch:	noarch

%description
This module allows you to deliberately hide modules from a program
even though they are installed. This is mostly useful for testing modules
that have a fallback when a certain dependency module is not installed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# pod2test is gone from perl-Test-Inline
perl -pi -e "s|pod2test|/bin/true|g" Makefile.PL

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/Test/Without
%{perl_vendorlib}/Test/Without/*
%{_mandir}/*/*

%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.170.0-1mdv2010.0
+ Revision: 405602
- rebuild using %%perl_convert_version

* Mon Jan 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2009.1
+ Revision: 331151
- update to new version 0.17

* Tue Oct 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2009.1
+ Revision: 295935
- update to new version 0.16

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.15-5mdv2009.0
+ Revision: 258598
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.15-4mdv2009.0
+ Revision: 246583
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 17 2007 Funda Wang <fundawang@mandriva.org> 0.15-2mdv2008.1
+ Revision: 109362
- rebuild

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2008.1
+ Revision: 104603
- update to new version 0.15

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.11-1mdv2008.0
+ Revision: 69250
- update to new version 0.11

* Thu May 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.09-1mdv2008.0
+ Revision: 22118
- 0.09


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.06-3mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.06-2mdk
- fix build

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.06-1mdk
- initial Mandriva package

