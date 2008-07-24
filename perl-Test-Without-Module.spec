%define real_name Test-Without-Module

Summary:	Test::Without::Module - Test fallback behaviour in absence of modules
Name:		perl-%{real_name}
Version:	0.15
Release: %mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Inline)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module allows you to deliberately hide modules from a program
even though they are installed. This is mostly useful for testing modules
that have a fallback when a certain dependency module is not installed.

%prep
%setup -q -n %{real_name}-%{version} 

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

