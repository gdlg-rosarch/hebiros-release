# Script generated with Bloom
pkgdesc="ROS - The hebiros package"


pkgname='ros-kinetic-hebiros'
pkgver='0.0.4_2'
pkgrel=1
arch=('any')
license=('TODO'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-message-generation'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-ros-control'
'ros-kinetic-ros-controllers'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=hebiros
source=()
md5sums=()

prepare() {
    cp -R $startdir/hebiros $srcdir/hebiros
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

