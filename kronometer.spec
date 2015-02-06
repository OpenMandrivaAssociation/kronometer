Name:		kronometer
Summary:	Stopwatch application built for the KDE
Version:	1.4.2
Release:	2
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.aelog.org/
Source0:	http://download.kde.org/stable/kronometer/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	desktop-file-utils
BuildRequires:	cmake

%description
Kronometer is a stopwatch application built 
for the KDE Desktop Environment.
Kronometer’s main features are the following:
Start/pause/resume stopwatch widget
Lap recording
Lap times sorting
Reset stopwatch and lap times
Time format settings
Times saving and resuming
Font and color customization
Lap times export.

%prep
%setup -q

%build
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=`kde4-config --prefix` \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo ..

%make

%install
make -C build DESTDIR=%buildroot install

chmod -x %{buildroot}%{_kde_applicationsdir}/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc README
%{_kde_docdir}/HTML
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_datadir}/apps/*
%{_kde_datadir}/*.kcfg
%{_kde_iconsdir}/*/*/*/kronometer.svgz
