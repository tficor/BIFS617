##########################################################################
# Author: Tracy Ficor       BIFS617                                      #
# Purpose: Search a dictionary                                           #
##########################################################################

EGR1_protein = {}

EGR1_protein['RLQ73868.1'] = "MAAAKAEMQLMSPLQISDPFGSFPHSPTMDNYPKLEEMMLLSNGAPQFLGAAGTPEGSGGGSSSSSSSGGGGGGGSNSGSSAFNPQGEPGEQPYEHLTTVVARRPLAWPLRFSSPSDLLFSNQASLLSFLPESFSDIALNNEKAMVETSYPSQTTRLPPITYTGRFSLEPAPNSGNTLWPEPLFSLVSGLVSMTNPPASSSSAPSPAASTSSSASQSPPLSCAVPSNDSSPIYSAAPTFPTPNTDIFPEPQSQAFPGSAGTALQYPPPAYPAAKGGFQVPMIPDYLFPQQQGDLGLGTPDQKPFQGLENRTQQPSLTPLSTIKAFATQSGSQDLKALNTTYQSQLIKPSRMRKYPNRPSKTPPHERPYACPVESCDRRFSRSDELTRHIRIHTGQKPFQCRICMRNFSRSDHLTTHIRTHTGEKPFACDICGRKFARSDERKRHTKIHLRQKDKKADKSVVASSATSSLSSYPSPVATSYPSPATTSFPSPVPTSYSSPGSSTYPSPAHSGFPSPSVATTYASVPPAFPAQVSSFPSAAVTNSFSTSTGLSDMTATFSPRTIEIC"
EGR1_protein['PRD35705.1'] = "MEKLNLAKDSVTCAREMCDLRFKHKFNLKRHYSVHTTEKLYECEVCGKRFKRKDDLKQHYITHSTEKPFVSKICLKEYKCYNIMCPLISKNNNFFENLMSV"
EGR1_protein['AAH72770.1'] = "MAVAKTEMLVSPLQISDPFSSFPHSPTMDNYPKLEEMMLLNAGGPQFLGASVPDGSGFNSTVEGAEQFDHLTADAFSEMSLSSEKALVESSYANQTTRLPSLTYTGRFSLEPATNSSNTLWPEPLFSLVSGLVGMANISPSSAPSSSPSSSSSSSSSQSPPLSCSVQSNDSSPIYSAAPTFPNSSSEIFPDHSPQPFQNASIPYPPPAYPVSKTTFQVPMIPDYLFPQQQGDVSLVSADQKPFQAMESRTQQPSLTPLSTIKAYATHTSQDLKTINSTYQSQIIKPSRMRKYPNRPSKTPPHERPYGCPVESCDRRFSRSDELTRHIRIHTGQKPFQCRICMRNFSRSDHLTTHIRTHTGEKPFACDICGRKFARSDERKRHTKIHLRQKDKKADKATPVSVASPVSSYSPSASTSYPSPVPTSYSSPVSSSYPSPVHSSFPSPTTAVTYPSVTSTFQTHGITSFPSSIMTNAFSSPMSSALSDMSLTYSPRTIEIC"

print("The available protein sequences are available RLQ73868.1, PRD35705.1, & AAH72770.1")
protein_seq = str(input("Type out one of the 3 accession number for EGR1: "))

seq = EGR1_protein.get(protein_seq, 0)

if seq == 0:
    print("Gene not found in this dictionary.")
else:
    print(seq)
    

