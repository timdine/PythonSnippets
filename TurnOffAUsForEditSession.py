<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<!DOCTYPE HTML>><HTML><HEAD>
<META content="text/html; charset=windows-1252" 
http-equiv="Content-Type"></HEAD>
<BODY><PRE>#############################
# Turn off AUs for Edit Session
# For the current user, disable ArcFM autoupdaters for the current edit session.
# Use carefully - this may disrupt business logic.
#
# Written by Skye Perry, ported to Python by Corey Blakeborough
# for SSP Innovations
# http://www.sspinnovations.com/
#
# Parameters:
# (none)
#############################

import Snippets
import comtypes
import ArcFM
from Snippets import CType
Snippets.GetDesktopModules()

ArcFM.GetModule("mmGeodatabase.olb")
from comtypes.gen.mmGeodatabase import *
mmAu2 = CType(MMAutoUpdater(), IMMAutoUpdater)
mmAu2.AutoUpdaterMode = mmAUMNoEvents

print 'AUs off!'
arcpy.AddMessage('AUs off!')</PRE></BODY></HTML>
