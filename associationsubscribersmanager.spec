%define name	 associationsubscribersmanager
%define oname    AssociationSubscribersManager 
%define version	 3.1
%define release	 %mkrel 1
%define Summary	 Software which allow people to easily manage their clubs


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	%oname-%version.tar.gz
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://kde-apps.org/content/show.php/kcm+tablet?content=114856
BuildRequires:	qt4-devel

%description
Association Subscribers Manager is a software which allow people 
to easily manage their clubs. The main goal is to make it simple.
Association Subscribers Manager do not require any database not 
any complicated settings.

If you are a in charge of a club and don't want a complicated 
software to manage it, you are in the right place !
In the other hand, if you are searching a collaborative web-based 
suite to manage your club you are clearly not at the right place !

%files
%defattr(-,root,root)
%_bindir/association_subscribers_manager
%_datadir/AssociationSubscribersManager

#---------------------------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Devel files needed to build apps based on %name

%description devel

%files devel
%defattr(-,root,root,-)
%_includedir/AssociationSubscribersManager

#---------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%version

%build
lrelease association_subscribers_manager.pro
%qmake_qt4 INSTALLDIR=%buildroot%_prefix
%make

%install
%__rm -rf %buildroot
%makeinstall_std

%clean
%__rm -rf %buildroot