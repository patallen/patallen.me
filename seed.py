from app import db
from app.models import *
dictlist=[
    {
	"author": 1,
	"title": "The One that Got Away",
	"body_md": """This is the body **with markdown**"""
    },
    {
	"author": 1,
	"title": "Oom Boom Boom, I Want You in My Room",
	"body_md": """Gotta get get [x3]
Gotta g-g-g-get-get-get get-get

Boom boom boom (Gotta get get) [x4]

Boom boom boom (now) [x2]
Boom boom boom [x2]

[Will.I.Am]
Yo
I got the hit that beat the block
You can get that bass overload
I got the that rock and roll
That future flow

That digital spit
Next level visual shit
I got that (Boom boom boom)
How the beat bang (Boom boom boom)"""
    },
    {
	"author": 1,
	"title": "This is MD Lorem!",
	"body_md": """Lorem markdownum miserum, pectora dicar, ora pondere fulget. Torrentem adest et
spretis cornuaque in parilesque toro, nec lumina voce simul parens. Obliquaque
victa [manu quatit](http://gifctrl.com/) est Thesea ventris commemorare artus
Theridamas Siculique insula; emissi. Certam spectandique habet et bibebatur enim
fit vidisti, per cura vinclisque securi: qua. Me totum truculenta frontem **in
indice** semper, multi longa amat: spectant resque.

Hirsutaque sanguine [luporum primaque](http://news.ycombinator.com/) et, ecquid
noviens? [Verbisque](http://omfgdogs.com/) recipit noctisque memorant amorem,
tibi cupiens: sua huius an tantum Rhexenore alimenta aper. **Cremabo suis**
potentum, procul, et est ille undis, ad! Quae promissa cresce heu nimium?

Exstantem coniunx destrinxit et, ostendens Tritoniaca. Lecti rates totidem,
recubare de similis veloxque passae; **exi** induco. [Nymphaeque alter
per](http://www.metafilter.com/) ignibus concita omnes arbitrium capitis primo
vultus ecquid nuribus."""
    }
]

for dict in dictlist:
    post = Post()
    for key, value in dict.items():
        setattr(post, key, value)

    db.session.add(post)
    db.session.commit()

p = User()
p.nickname = "Pat"
p.first_name = "Patrick"
p.last_name = "Allen"
p.location = "Windham, NH"
p.password = "password"

db.session.add(p)
db.session.commit()