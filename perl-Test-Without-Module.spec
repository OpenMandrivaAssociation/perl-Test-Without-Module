%define upstream_name    Test-Without-Module
%define upstream_version 0.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Test::Without::Module - Test fallback behaviour in absence of modules
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Test::Inline)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module allows you to deliberately hide modules from a program
even though they are installed. This is mostly useful for testing modules
that have a fallback when a certain dependency module is not installed.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# pod2test is gone from perl-Test-Inline
perl -pi -e "s|pod2test|/bin/true|g" Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/Test/Without
%{perl_vendorlib}/Test/Without/*
%{_mandir}/*/*
