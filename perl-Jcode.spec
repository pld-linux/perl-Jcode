#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Jcode
Summary:	Jcode - Japanese Charset Handler
Summary(pl):	Jcode - obs³uga japoñskiego kodowania
Name:		perl-Jcode
Version:	0.82
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/D/DA/DANKOGAI/%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-MIME-Base64
%endif
# this *should not* be needed...
Provides:	perl(Jcode::Constants)
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
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
