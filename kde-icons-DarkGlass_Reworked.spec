%define		_name		DarkGlass_Reworked
Summary:	KDE Icons Theme - %{_name}
Summary(pl.UTF-8):	Motyw ikon dla KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	2.72
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://www.mentalrey.it/icon_set/%{_name}.tar.gz
# Source0-md5:	c235381774255536acbe7d9ccbba54f2
URL:		http://www.kde-look.org/content/show.php/DarkGlass_Reworked?content=67902
BuildRequires:	ImageMagick
BuildRequires:	ImageMagick-coder-png
BuildRequires:	rpmbuild(macros) >= 1.123
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Icons Theme - %{_name}.

%description -l pl.UTF-8
Motyw ikon dla KDE - %{_name}.

%prep
%setup -q -n %{_name}
./buildset

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xfj %{_name}.tar.bz2 -C $RPM_BUILD_ROOT%{_iconsdir}
install index.desktop $RPM_BUILD_ROOT%{_iconsdir}/%{_name}

rm -f `find $RPM_BUILD_ROOT -name .directory`

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_iconsdir}/%{_name}
