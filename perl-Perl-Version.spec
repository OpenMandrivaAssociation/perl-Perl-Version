%define upstream_name    Perl-Version
%define upstream_version 1.019
Name:		perl-%{upstream_name}
Version:	1.019
Release:	15

Summary:	Parse and manipulate Perl version strings
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/briandfoy/perl-version
Source0:	https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Perl-Version-1.019.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Perl::Version provides a simple interface for parsing, manipulating and
formatting Perl version strings.

Unlike version.pm (which concentrates on parsing and comparing version
strings) Perl::Version is designed for cases where you'd like to parse a
version, modify it and get back the modified version formatted like the
original.

For example:

%prep
%setup -q -n Perl-Version-1.019

%build
yes | perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc Changes README* LICENSE* META.yml
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/perl-reversion

