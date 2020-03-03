###############################################
# TX SX Pro Custom Payload Packer - by CTCaer #
###############################################

import struct
import hashlib
from os import unlink

"""
typedef struct boot_dat_hdr
{
	unsigned char ident[0x10];
	unsigned char sha2_s2[0x20];
	unsigned int s2_dst;
	unsigned int s2_size;
	unsigned int s2_enc;
	unsigned char pad[0x10];
	unsigned int s3_size;
	unsigned char pad2[0x90];
	unsigned char sha2_hdr[0x20];
} boot_dat_hdr_t;
"""

def sha256(data):
	sha256 = hashlib.new('sha256')
	sha256.update(data)
	return sha256.digest()
	
boot_fn = 'boot.dat'
# Custom payload filename.
stage2_fn = 'fusee-primary.bin'

boot = open(boot_fn, 'wb')

with open(stage2_fn, 'rb') as fh:
	stage2 = bytearray(fh.read())
	stage2 = bytes(stage2)

# Re-create the header.
header = b''

# Magic ID.
header += b'\x43\x54\x43\x61\x65\x72\x20\x42\x4F\x4F\x54\x00'

# Version 2.5.
header += b'\x56\x32\x2E\x35'

# Set sha256 hash of stage2 payload.
header += sha256(stage2)

# Set stage2 payload destination to 0x40010000.
header += b'\x00\x00\x01\x40'

# Stage2 payload size.
header += struct.pack('I', len(stage2))

# Disable Stage2 encryption.
header += struct.pack('I', 0)

# Add padding. Stage3 size is 0.
header += b'\x00' * 0xA4

# Add header's sha256 hash.
sha256 = hashlib.new('sha256')
sha256.update(header)
header += sha256.digest()

# Write header and the plaintext custom payload.
boot.write(header)
boot.write(stage2)

boot.close()