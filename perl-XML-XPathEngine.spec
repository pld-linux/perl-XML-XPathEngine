#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	XPathEngine
Summary:	XML::XPathEngine - a re-usable XPath engine for DOM-like trees
Summary(pl.UTF-8):	XML::XPathEngine - silnik XPath dla drzew w stylu DOM
Name:		perl-XML-XPathEngine
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	225f53d420d4fca50cd9d18b877780d6
URL:		http://search.cpan.org/dist/XML-XPathEngine/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an XPath engine, that can be re-used by other
module/classes that implement trees.

In order to use the XPath engine, nodes in the user module need to
mimick DOM nodes. The degree of similitude between the user tree and a
DOM dictates how much of the XPath features can be used. A module
implementing all of the DOM should be able to use this module very
easily (you might need to add the cmp method on nodes in order to get
ordered result sets). 

%description -l pl.UTF-8
Ten moduł udostępnia silnik XPath, który można wykorzystywać w innych
modułach/klasach implementujących drzewa.

W celu użycia silnika XPath węzły w module użytkownika muszą
naśladować węzły DOM. Stopień podobieństwa między drzewem użytkownika
a drzewem DOM określa jak wiele możliwości XPath można wykorzystać.
Moduł implementujący całość DOM powinien być w stanie bardzo łatwo
użyć tego modułu (może zajść potrzeba dodania metody cmp dla węzłów w
celu uzyskania uporządkowanych zbiorów wyników).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/XPathEngine
%{_mandir}/man3/*
