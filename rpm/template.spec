Name:           ros-kinetic-x-demo
Version:        0.0.3
Release:        0%{?dist}
Summary:        ROS x_demo package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-hebiros-description
Requires:       ros-kinetic-joint-state-publisher
Requires:       ros-kinetic-moveit-kinematics
Requires:       ros-kinetic-moveit-planners-ompl
Requires:       ros-kinetic-moveit-ros-move-group
Requires:       ros-kinetic-moveit-ros-visualization
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-xacro
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-hebiros-description

%description
An automatically generated package with all the configuration and launch files
for using the arm_demo with the MoveIt! Motion Planning Framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Nov 29 2017 Xavier Artache <x@hebirobotics.com> - 0.0.3-0
- Autogenerated by Bloom

