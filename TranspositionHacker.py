
import pyperclip, detectEnglish, transposition_decrypt

def main():
    # You might want to copy & paste this text from the source code at
    # https://www.nostarch.com/crackingcodes/:
    #myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""
    myMessage="""Rrh ilneanneta kh r fs  img ty  il oennr rlfc eaauutherysesc geiti h t et wo arnuhhenwsnehp  tfm e oaa zlrutl le tke pnsgsenoddhdaro e ntedeih sottR.eowaouwhpidtr tralda ni s hu i e.eas fsmji r stef.wehe crarfla ln hnd i ferwenttotnfcts  r h oaocs nsh l  rii tes  dytagge aagw,siir h f. reho ckaemribaesa  wy t nkT   ft  hn lrty ha onngdet  wo elSo  rotn teltnhaiSofgootssohofa.aa.odctshlgdye hs asa ahlsv r  wimiueesnh rs-doiurenrt td  rl  aa o spenIsteotedoebnojao grvr gefo 1a np  lo   l leashptowfpa on esti , ruifosnshee a  lmp0ypcptdymsFfyReawhupiu ietew odthod pytn y stt,rdlawy r  reoha  oel yam omyotaerhx cu henite  gsfh rl  usea Feawa seyptuyyhlv dum n tlastfotler.dhrbtstue–aybitorstettocte .uhnrieaewilid o dt rrn,atw  ehah rla n uni i hyt uthdf ledinl  hgdneoftsiceot nii n adege.dwgittetalerytlie i l eagpwhe egsu h olmmrgdcsSosp san  hen esrle i hdc trI gd   eenir pttefnee ais ehtnspevgHoi thr a aGase ewosfFu waRnr n.tish i a lsvct e o l etefcgref–ivry l b e t eylanyt stotiesgtraatiaob lwtak hr hiore nenrsomesab sysisdl sho ed mho ms npulsi,hcih  c vv rbehioiwo otehhr…k  atle h etat aottgeceik ienetmomeeseudin-n mpmh aei eaw oi het,hlikgu h  hageos droaminrhdt cgCcoeeeecl aY mof gfe"""
    hackedMessage=hackTransposition(myMessage)

    if hackedMessage==None:
        print("Failed to hack Encryption")
    else:
        print("Copying hacked message to clipboard")
        print(hackedMessage)
        pyperclip.copy(hackedMessage)

def hackTransposition(message):
    print("Hacking...")

    print("press control+c to end program")

    #brute force every key

    for key in range(1,len(message)):
        print("trying key #%s..." %(key))
        decryptedText=transposition_decrypt.decryptMessage(key,message)
        if detectEnglish.isEnglish(decryptedText):
            #ask if correct decrypt
            print()
            print("possible hack")
            print("key %s: %s" %(key, decryptedText[:100]))
            print()
            print("Enter D if done, anything else continues hacking")
            response=input("> ")
            if response.strip().upper().startswith("D"):               
                return decryptedText
    return None

if __name__=="__main__":
    main()
