/*

BERGCloud library for Linux

Copyright (c) 2013 BERG Cloud Ltd. http://bergcloud.com/

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

*/

#ifndef BERGCLOUDLINUX_H
#define BERGCLOUDLINUX_H

#include "BERGCloudBase.h"
#include <pthread.h>
#include <string>

class BERGCloudLinux : public BERGCloudBase
{
public:
  void begin(const char *SPIpath);
  void end();
  using BERGCloudBase::display;
  /* Methods using std::string class */
  bool display(std::string& s);
  /* Methods using pointers, for SWIG */
  bool getClaimcode(const char *claimcode);
  bool getEUI64(uint8_t type, uint8_t *eui64);
  bool getDeviceAddress(uint8_t *address);
private:
  uint16_t SPITransaction(uint8_t *dataOut, uint8_t *dataIn, uint16_t dataSize, bool finalCS);
  uint32_t _timer_ms(void);
  void timerReset(void);
  uint32_t timerRead_mS(void);
  uint16_t getHostType(void);
  void lockTake(void);
  void lockRelease(void);
  int spi;
  uint32_t resetTime;
  static pthread_mutex_t spiLock;
};

#endif // #ifndef BERGCLOUDLINUX_H
