#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Jcode
Summary:	Jcode - Japanese charset handler
Summary(pl):	Jcode - obs³uga kodowania japoñskiego
Name:		perl-Jcode
Version:	0.83
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/D/DA/DANKOGAI/%{pnam}-%{version}.tar.gz
# Source0-md5:	64e137e289e9fc65c1afc00c08ffa0f3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MIME-Base64
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jcode is a Perl extension interface to convert Japanese text.

%description -l pl
Jcode jest rozszerzeniem Perla do konwersji tekstu japoñskiego.

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
%dir %{perl_vendorarch}/Jcode
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/Jcode/*.pm
%{perl_vendorarch}/Jcode/Unicode
%dir %{perl_vendorarch}/auto/Jcode
%dir %{perl_vendorarch}/auto/Jcode/Unicode
%attr(755,root,root) %{perl_vendorarch}/auto/Jcode/Unicode/*.so
%{perl_vendorarch}/auto/Jcode/Unicode/*.bs
%{_mandir}/man3/*
