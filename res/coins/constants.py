#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This file is for the storage of constants

# This part is for constants related to Opal Kelly

OK_ADDR_COMMAND=0x00
OK_ADDR_DATA=0x01

# Correspond to OK_ADDR_COMMAND
OK_STORE_1=0x01
OK_STORE_2=0x02
OK_DISPLAY=0x03

# Correspond to OK_ADDR_DATA
OK_DATA_1=0x01
OK_DATA_2=0x02

# OK triggers
OK_ADDR_TRIGGER=0x40

# Correspond to OK_ADDR_TRIGGER
OK_DATA_TRIGGER=0x00

# ----------------------------------------------------
# Below are constant configurations for Bioee_fpga.bit
# ----------------------------------------------------

# Address for communication using opal kelly
OK_ADDR_WIN_CTRL0 = 0x00
OK_ADDR_WIN_CTRL1 = 0x01
OK_ADDR_WIN_CTRL2 = 0x02

OK_ADDR_WOUT_USELESS = 0x20

OK_ADDR_TRIGIN = 0x40
OK_ADDR_TRIGOUT = 0x60

OK_ADDR_PIPEIN_ADC = 0x80
OK_ADDR_PIPEIN_DAC = 0x81
OK_ADDR_PIPEOUT = 0xA0

# Corresponding data:
# Data for wirein, control 0
OK_DATA_WIN_CTRL0_RESET = 0x8000
OK_DATA_WIN_CTRL0_DACENABLE = 0x0080
OK_DATA_WIN_CTRL0_NULL = 0x0000

# Basic bit configuration
BIT_0	 = 0x0001
BIT_1	 = 0x0002
BIT_2	 = 0x0004
BIT_3	 = 0x0008
BIT_4	 = 0x0010
BIT_5	 = 0x0020
BIT_6	 = 0x0040
BIT_7	 = 0x0080
BIT_8	 = 0x0100
BIT_9	 = 0x0200
BIT_10 = 0x0400
BIT_11 = 0x0800
BIT_12 = 0x1000
BIT_13 = 0x2000
BIT_14 = 0x4000
BIT_15 = 0x8000

# This part is related to constants defining the position of all control bits:

# Default value for all control signals
TIA_FB_UNITY		= 0
TIA_FB_5P				= 0
TIA_FB_1P				= 1
TIA_FB_500F			= 0
TIA_FB_250F			= 0
TIA_FB_10M			= 1
TIA_FB_1M				= 1
TIA_FB_100K			= 0
TIA_FB_10K			= 0
TIA_COMP_CAPBYP	= 0
TIA_COMP_RESBYP	= 0
TIA_COMP_CAP1		= 0
TIA_COMP_CAP2		= 0
TIA_COMP_100K		= 0
TIA_COMP_10K 		= 0
TIA_VCM					= 1
TIA_OTATEST			= 0
TIA_CELLTEST 		= 0
TIA_WE 				  = 1
CA_COMP_CAP			= 1
CA_COMP_10K			= 1
CA_COMP_1K 			= 0
CA_COMP_100 		= 0
CA_RESBYP				= 0
CA_CESETEXT			= 0
CA_CEINT				= 1
CA_CEEXT 				= 0
CA_UNITY				= 0
CA_REEXT 				= 1
CA_REINT				= 0

# Set the control signal values using external configuration file
# PFN

# Assemble the control bits into a vector
OK_CTRLVEC1 = CA_COMP_CAP 		* BIT_0  + CA_COMP_10K 		* BIT_1  	+ CA_COMP_1K 		* BIT_2  	+ CA_COMP_100 	 	* BIT_3  + \
							CA_RESBYP 			*	BIT_4  + CA_CESETEXT 		* BIT_5  	+ CA_CEINT 	 		* BIT_6  	+ CA_CEEXT 				* BIT_7  + \
							CA_UNITY 				* BIT_8  + CA_REEXT		 		* BIT_9  	+ CA_REINT 			* BIT_10 	+ TIA_WE 					* BIT_11 + \
							TIA_CELLTEST		* BIT_12 + TIA_OTATEST 		* BIT_13 	+ TIA_VCM 			* BIT_14 	+ TIA_FB_10K   		* BIT_15

OK_CTRLVEC2 = TIA_COMP_100K 	* BIT_0	 + TIA_COMP_CAP1 	* BIT_1 	+ TIA_COMP_CAP2 * BIT_2 	+ TIA_COMP_RESBYP * BIT_3 + \
							TIA_COMP_CAPBYP * BIT_4	 + TIA_FB_10K 		* BIT_5 	+ TIA_FB_100K 	* BIT_6 	+ TIA_FB_1M 			* BIT_7 + \
							TIA_FB_10M 			* BIT_8	 + TIA_FB_250F 		* BIT_9 	+ TIA_FB_500F 	* BIT_10 	+ TIA_FB_1P 			* BIT_11 + \
							TIA_FB_5P 			* BIT_12 + TIA_FB_UNITY 	* BIT_13

OK_CHANNELMAP = [[1, 4], [1, 3], [1, 2], [1, 6], [1, 5], [1, 7],
								 [0, 3], [0, 4], [0, 0], [0, 5], [0, 2], [0, 6], [0, 1], [0, 7],
								 [4, 3], [4, 2], [4, 0], [4, 4], [4, 5], [4, 1], [4, 7], [4, 6],
								 [3, 3], [3, 5], [3, 2], [3, 0], [3, 4], [3, 7], [3, 1], 
								 [2, 3], [2, 5], [2, 0], [2, 7], [2, 2], 
								 [3, 6],
								 [2, 1], [2, 6], [2, 4],
								 [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7],
								 [1, 0], [1, 1]]


