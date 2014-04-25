%define upstream_name    Perl-Version
%define upstream_version 1.013

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Parse and manipulate Perl version strings

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(File::Slurp::Tiny)
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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
yes | perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/perl-reversion


