Name:		kronometer
Summary:	Stopwatch application built for the KDE
Version:	2.0.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		http://www.aelog.org/
Source0:	http://download.kde.org/stable/kronometer/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)

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
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}

%files -f %{name}.lang
%doc README
%{_kde_docdir}/HTML
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_datadir}/apps/*
%{_kde_datadir}/*.kcfg
%{_kde_iconsdir}/*/*/*/kronometer.svgz
