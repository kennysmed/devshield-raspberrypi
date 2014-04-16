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

#include <unistd.h>
#include <stdio.h>
#include <stdarg.h>
#include <stdint.h>
#include <stdlib.h>
#include <fcntl.h>
#include <time.h>
#include <sys/ioctl.h>
#include <linux/spi/spidev.h>
#include <string.h>

#include "BERGCloudLinux.h"

pthread_mutex_t BERGCloudLinux::spiLock =  PTHREAD_MUTEX_INITIALIZER;

uint16_t BERGCloudLinux::SPITransaction(uint8_t *dataOut, uint8_t *dataIn, uint16_t dataSize, bool finalCS)
{
  struct spi_ioc_transfer tr = {0};
  int result;

  if ( (dataOut == NULL) || (dataIn == NULL) || (spi < 0) )
  {
    _LOG("Invalid parameter (BERGCloudLinux::SPITransaction)\r\n");
    _LOG("The SPI interface may not be initialised.\r\n");
    exit(0);
  }

  tr.bits_per_word = 8;
  tr.len = dataSize;
  tr.rx_buf = (__u64)dataIn;
  tr.tx_buf = (__u64)dataOut;
  tr.speed_hz = 4000000;
  tr.cs_change = finalCS;

  result = ioctl(spi, SPI_IOC_MESSAGE(1), &tr);

  if (result < 0)
  {
    _LOG("SPI ioctl returned < 0 (BERGCloudLinux::SPITransaction)\r\n");
    _LOG("The SPI interface may not be initialised.\r\n");
    exit(0);
  }

  return dataSize;
}

uint32_t BERGCloudLinux::_timer_ms(void)
{
  struct timespec ts;
  uint32_t time_ms;

  clock_gettime(CLOCK_MONOTONIC, &ts);
  time_ms = (ts.tv_sec * 1000UL) + (ts.tv_nsec / 1000000UL);
  return time_ms;
}

void BERGCloudLinux::timerReset(void)
{
  resetTime = _timer_ms();
}

uint32_t BERGCloudLinux::timerRead_mS(void)
{
  return _timer_ms() - resetTime;
}

void BERGCloudLinux::begin(const char *SPIpath)
{
  /* Call base class method */
  BERGCloudBase::begin();

  if (SPIpath == NULL)
  {
    _LOG("'SPIpath' is NULL (CBERGCloudLinux::begin)\r\n");
  }

  /* Configure SPI */
  spi = open(SPIpath, O_RDWR);

  if (spi < 0)
  {
    _LOG("Can't open SPI device (BERGCloudLinux::begin)\r\n");
  }
}

void BERGCloudLinux::end()
{
  /* Deconfigure SPI */
  if (spi >= 0)
  {
    close(spi);
  }

  /* Call base class method */
  BERGCloudBase::end();
}

bool BERGCloudLinux::display(std::string& s)
{
  return display(s.c_str());
}

uint16_t BERGCloudLinux::getHostType(void)
{
  return BC_HOST_LINUX;
}

/* The following methods are a temporary workaround */
/* for issues dealing with references in SWIG. */

bool BERGCloudLinux::getClaimcode(const char *claimcode)
{
  char temp[BC_CLAIMCODE_SIZE_BYTES];
  bool result;

  result = BERGCloudBase::getClaimcode(temp);

  if (result)
  {
    memcpy((void *)claimcode, temp, sizeof(temp));
  }

  return result;
}

bool BERGCloudLinux::getEUI64(uint8_t type, uint8_t *eui64)
{
  uint8_t temp[BC_EUI64_SIZE_BYTES];
  bool result;

  result = BERGCloudBase::getEUI64(type, temp);

  if (result)
  {
    memcpy(eui64, temp, sizeof(temp));
  }

  return result;
}

bool BERGCloudLinux::getDeviceAddress(uint8_t *address)
{
  uint8_t temp[BC_ADDRESS_SIZE_BYTES];
  bool result;

  result = BERGCloudBase::getDeviceAddress(temp);

  if (result)
  {
    memcpy(address, temp, sizeof(temp));
  }

  return result;
}

void BERGCloudLinux::lockTake(void)
{
  pthread_mutex_lock(&spiLock);
}

void BERGCloudLinux::lockRelease(void)
{
  pthread_mutex_unlock(&spiLock);
}
