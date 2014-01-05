%define upstream_name    Debug-Client
%define upstream_version 0.29

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Client side code for perl debugger
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Debug/Debug-Client-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(PadWalker)
BuildRequires:	perl(Term::ReadLine)
BuildRequires:	perl(Term::ReadLine::Perl)
BuildRequires:	perl(Test::Class)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
new
    The constructor can get two parameters: host and port.

      my $d = Debug::Client->new;
    
      my $d = Debug::Client->new(host => 'remote.hots.com', port => 4242);

    Immediately after the object creation one needs to call

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Disable for now
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 653404
- rebuild for updated spec-helper

* Thu Dec 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 482083
- import perl-Debug-Client


* Thu Dec 24 2009 cpan2dist 0.11-1mdv
- initial mdv release, generated with cpan2dist

