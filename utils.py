from genericpath import isdir
import sys
import pathlib
import logging
import traceback
global DEBUG
DEBUG = True

try:
    #import colorama
    from colorama import init
    init()
    from colorama import Fore, Back, Style
    COLOR = True
except ImportError as derp:
    print("[-] NO COLOR PRINTING FUNCTIONS AVAILABLE, Install the Colorama Package from pip")
    COLOR = False

################################################################################
##############               LOGGING AND ERRORS                #################
################################################################################
log_file            = 'logfile'
logging.basicConfig(filename=log_file, 
                    #format='%(asctime)s %(message)s', 
                    filemode='w'
                    )
logger              = logging.getLogger()
launchercwd         = pathlib.Path().absolute()

redprint          = lambda text: print(Fore.RED + ' ' +  text + ' ' + Style.RESET_ALL) if (COLOR == True) else print(text)
blueprint         = lambda text: print(Fore.BLUE + ' ' +  text + ' ' + Style.RESET_ALL) if (COLOR == True) else print(text)
greenprint        = lambda text: print(Fore.GREEN + ' ' +  text + ' ' + Style.RESET_ALL) if (COLOR == True) else print(text)
yellowboldprint = lambda text: print(Fore.YELLOW + Style.BRIGHT + ' {} '.format(text) + Style.RESET_ALL) if (COLOR == True) else print(text)
makeyellow        = lambda text: Fore.YELLOW + ' ' +  text + ' ' + Style.RESET_ALL if (COLOR == True) else None
makered           = lambda text: Fore.RED + ' ' +  text + ' ' + Style.RESET_ALL if (COLOR == True) else None
makegreen         = lambda text: Fore.GREEN + ' ' +  text + ' ' + Style.RESET_ALL if (COLOR == True) else None
makeblue          = lambda text: Fore.BLUE + ' ' +  text + ' ' + Style.RESET_ALL if (COLOR == True) else None
debugred = lambda text: print(Fore.RED + '[DEBUG] ' +  text + ' ' + Style.RESET_ALL) if (DEBUG == True) else None
debugblue = lambda text: print(Fore.BLUE + '[DEBUG] ' +  text + ' ' + Style.RESET_ALL) if (DEBUG == True) else None
debuggreen = lambda text: print(Fore.GREEN + '[DEBUG] ' +  text + ' ' + Style.RESET_ALL) if (DEBUG == True) else None
debugyellow = lambda text: print(Fore.YELLOW + '[DEBUG] ' +  text + ' ' + Style.RESET_ALL) if (DEBUG == True) else None
debuglog     = lambda message: logger.debug(message) 
infolog      = lambda message: logger.info(message)   
warninglog   = lambda message: logger.warning(message) 
errorlog     = lambda message: logger.error(message) 
criticallog  = lambda message: logger.critical(message)

def debugprint(message:str):
    if DEBUG== True:
        debugyellow(f"[DEBUG] {message}")
    else:
        None

################################################################################
##############             ERROR HANDLING FUNCTIONS            #################
################################################################################
def errorlogger(message):
    """
    prints line number and traceback
    TODO: save stack trace to error log
            only print linenumber and function failure
    """
    exc_type, exc_value, exc_tb = sys.exc_info()
    trace = traceback.TracebackException(exc_type, exc_value, exc_tb) 
    lineno = 'LINE NUMBER : ' + str(exc_tb.tb_lineno)
    logger.error(
        redprint(
            message+"\n [-] "+lineno+"\n [-] "+''.join(trace.format_exception_only()) +"\n"
            )
        )
