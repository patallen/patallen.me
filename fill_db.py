from app import db
from app.models import Post, User, Project

db.create_all()

user = User()
user.nickname = "Pat"
user.first_name = "Patrick"
user.last_name = "Allen"
user.location = "Windham, NH"
db.session.add(user)

post = """# Obprobrium meas

## Proturbat poscit causa hunc gradientis cornua fratri

Lorem markdownum Mycenae, nec simul latratibus facibus denique nubemque possunt?
Quoque vestra abstrahere Cyllenius et dant Chrysenque Phaethon exspirare
superstitibus mortemque ramum patriaque posti.

- Mihi ferro quamvis numen exstinctos si pelago
- Non vidi loci quem tu alebat bifores
- Tubere carissime dedecus ordine
- Crimina timor puerilem rates ad exilium diversa
- Est pugnes cura animo
- Et enim ausim

Reducto tuos unco vacet Lycabas et mens. Ales sed haec pendebat tu quem; tergo
dea umbras Gorgone infraque. Undis de animus adeundi ducunt est concubitus
ducere. Me meliora factum, pro crescentesque cruore.

## Mentique cerebrum meus Venere tua superare illis

Magni mirum excipit inplevere virique inquit Nelei, revirescere Ilion coniunx
**ingemuit**, haut simul, si apium adituque sed. Penetraret Apolline inductas
tamen pro commoda pars, dapibus si, in me vacuo quaerenti ecce, radicibus! Rore
erit unus habitat fluctibus aliisque cepit, ut ubi corpore, re? Ecce
fraternaeque hic qui, vota vigil fecistis nupta, Andraemon candore carmen
dicere, comitantibus quod vastarumque egit.

Porrexi incessere moenibus: [volentem](http://zombo.com/) simulat salus, ense
facto cui. Adest monstri Vesta ferendo crines officium, et videoque virgo,
tandemque dixit, duro auras, soceri, quoque? Etiam et
[multae](http://eelslap.com/) iamque pariter, tua pello mille undas illa medio
funeris; opes altera suem coniuge.

    malware.data(-1);
    if (card_dashboard.hsf(sdk * wi_thunderbolt_servlet, socket_skin,
            waveformHibernateText)) {
        office_eps_snmp = plain;
        word_python.dlc_directory = rdramCorrectionDvd.nocSecondaryEdi(recycle,
                layoutMap, software(251498, thumbnail_class));
        searchBannerHard.designWebsiteIrc = panel;
    } else {
        fragmentation_joystick -= drive_ccd.miniTableAbend(2);
        floating_storage.compression_simm_core +=
                simplex_web.osdModifierMinicomputer.processor(cifs +
                syn_prebinding, driver, googleSpriteText(sync,
                data_telecommunications_import, google));
    }
    serp_raid_trackback = roomSector;
    if (pageNameDial - 4) {
        white_graphic_friendly = publishing(motherboardFontDisk,
                oasis.yottabyte_gbps_subdirectory(plugView));
        wamp_swappable_alu = tagApacheBookmark(83, control, kilohertz(default,
                ddl, cc_grep_newline));
    }
    var camera_operating_push = token_pci_offline(node, 4, dynamic_multi_pc);

Atque summissoque sine loquentem Hector hortatibus ingemuit vincis casside
multaque. Per mittitur nomina quae, alte praemia!"""
p1 = Post()
p1.author = user.id
p1.title = "To the Candy Shop!"
p1.body_md = post
db.session.add(p1)

p2 = Post()
p2.author = user.id
p2.title = "The bee's knees"
p2.body_md = '__Sometimes__, **I like food**'
db.session.add(p2)

db.session.commit()
