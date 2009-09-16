#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Jcode
Summary:	Jcode - Japanese charset handler
Summary(pl.UTF-8):	Jcode - obsługa kodowania japońskiego
Name:		perl-Jcode
Version:	2.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DANKOGAI/%{pnam}-%{version}.tar.gz
# Source0-md5:	f6c52253ff69a44c38a9183c469f6eb0
URL:		http://search.cpan.org/dist/Jcode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MIME-Base64
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jcode is a Perl extension interface to convert Japanese text.

%description -l pl.UTF-8
Jcode jest rozszerzeniem Perla do konwersji tekstu japońskiego.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Jcode
%{_mandir}/man3/*
