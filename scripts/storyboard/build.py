#!/usr/bin/env python3
"""EP05 The Color You Were Told to Wear — storyboard builder.
Writes storyboard.json, char_cards.json, vo_chapters.txt. Asserts VO lines == script text."""
import json, re, os

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, '..', 'ep05_script.md')

STYLE = ('flat 2D hand-drawn digital cartoon illustration, thick smooth black marker outlines of even weight with a slightly wobbly hand-drawn feel and rounded line ends, deadpan doodle explainer style, flat muted pastel color fills with no gradients, no shading and no cast shadows, soft desaturated palette of cream beige, sage green, periwinkle lavender, pale butter yellow, dusty blue, baby blue, soft pastel pink, light and mid gray, warm tan brown and slate blue with a single warm amber accent, simple flat background of either one solid pastel wall color above a pale cream floor separated by a single horizontal line, or a plain off-white empty background, minimal simplified props, lots of empty negative space, no letters or words anywhere unless a specific short word is given in quotes in this prompt (then letter exactly that word in clean bold hand-drawn capitals and nothing else), papers and pages that should hold writing show neat rows of gray scribble lines instead of being blank, no logos or brand names, every face drawn completely with two equal eyes, a nose and one mouth, everyone fully and modestly clothed, 16:9 horizontal composition.')

CROWD = ('Every person in the picture, including babies, children, small background figures and crowds, is drawn in exactly the same channel character style and proportions as the main characters: big round white head, two equal round eyes with dot pupils, a tiny nose, one small mouth, a real clothed body, and colored hair (brown, black, auburn, blonde or gray, never plain white); distant people are smaller only because of perspective, never simplified, faceless or silhouetted.')

FACE = ('a large perfectly round white head outlined in thick black marker, {head}, two equal-sized fairly large round white eyes outlined in black each with a small black dot pupil, small curved eyebrows, a tiny simple nose drawn as one small curved line, exactly one small smooth continuous unbroken mouth fully inside the face below the eyes, no ears, a real simple soft rounded body in clothes (not a stick figure), clothing drawn as flat color shapes with black outlines, small round hands')
ADULT = 'about one third of the total body height'
KID = 'about half of the total body height, a small chubby child body'
LASH = ', three tiny eyelashes on each eye'

def ch(name, intro, look, kid=False, woman=False):
    return dict(name=name, desc=f"{intro} has " + FACE.format(head=KID if kid else ADULT) + (LASH if woman else '') + ', ' + look + '.')

CHARS = {
 'V': ch('Victorian mother', 'The Victorian mother', 'chestnut brown hair in a neat low bun, a long high-collared sage green 1880s dress with long sleeves and a small cream lace collar', woman=True),
 'B': ch('Victorian toddler boy', 'The Victorian toddler boy (about three years old)', 'shoulder-length wavy brown curls, a knee-length cream baby dress with a lace hem and small brown button boots', kid=True),
 'K': ch('1918 baby-store owner', 'The 1918 baby-store owner is a middle-aged man who', 'short dark brown hair parted in the middle, a small brown mustache, small round spectacles, a tan waistcoat over a cream shirt with rolled sleeves, and a slate blue bow tie'),
 'M': ch('1927 young mother', 'The 1927 young mother', 'a sleek black bob under a dusty blue cloche hat, a knee-length warm tan 1920s coat dress with amber buttons', woman=True),
 'R': ch('1950s mother', 'The 1950s mother', 'short golden blonde curled 1950s hair, a soft pastel pink shirtwaist dress with a full skirt and a small cream apron', woman=True),
 'S': ch('1970s mother', 'The 1970s mother', 'long straight auburn hair parted in the middle, a mustard yellow turtleneck and brown corduroy flared trousers', woman=True),
 'T': ch('1970s toddler', 'The 1970s toddler', 'messy light brown hair, a dusty red and butter yellow striped shirt and denim overalls', kid=True),
 'W': ch('1980s mother', 'The 1980s mother', 'big curly dark brown permed hair, an oversized periwinkle lavender sweater and slate blue jeans', woman=True),
 'D': ch('1980s father', 'The 1980s father is a man who', 'short brown hair, a thick brown mustache, a slate blue polo shirt and tan trousers'),
 'H': ch('modern woman', 'The modern woman', 'shoulder-length dark brown hair tied in a low ponytail, a mustard yellow knit sweater, slate blue jeans and small white sneakers', woman=True),
 'L': ch('modern boy', 'The modern boy (about four years old)', 'short black hair, a dusty blue t-shirt and tan shorts', kid=True),
 'G': ch('modern girl', 'The modern girl (about six years old)', 'golden blonde hair in two pigtails, a sage green t-shirt and slate blue leggings', kid=True, woman=True),
}

# (chapter, vo, scene, chars, crowd, anim)
S = []
def s(chp, vo, scene, chars='', crowd=False, anim=''):
    S.append(dict(chapter=chp, vo=vo, scene=scene, chars=list(chars), crowd=crowd, anim=anim))

C='Hook'
s(C,"In nineteen eighteen, a magazine for baby stores gave parents a simple rule:","Medium shot: the 1918 baby-store owner stands behind a wooden shop counter, holding up an open magazine toward the viewer with a serious face; behind him shelves of small folded baby clothes; the magazine cover shows \"1918\".",'K',anim="The man lifts the magazine a little higher toward the camera and gives one firm nod.")
s(C,"pink is for boys.","Close-up on a plain off-white background: a tiny soft pastel pink baby romper on a wooden hanger with a small paper tag reading \"BOYS\".")
s(C,"Blue is for girls.","Close-up on a plain off-white background: a tiny baby blue romper on a wooden hanger with a small paper tag reading \"GIRLS\".")
s(C,"It wasn't a joke, and it wasn't a mistake.","Close-up: the 1918 baby-store owner behind the counter raises one finger, perfectly deadpan, completely serious.",'K')
s(C,"It was the advice of the day, printed for the people who sold baby clothes.","Wide shot: an old 1910s printing press rolling out magazine pages covered in neat gray scribble lines, a tall stack of finished magazines tied with string beside it, a printer in a cap and apron working the lever.",'',True)
s(C,"So how did the color for boys become the color for girls in just a few decades?","Infographic on off-white: on the left a pink paint swatch above a small toddler boy icon and the label \"1918\"; a big hand-drawn amber arrow curves to the right, where the same pink swatch sits above a small toddler girl icon and the label \"TODAY\".")
s(C,"And who decided that a newborn needs a color at all?","Front view at eye level: a chubby baby in a plain cream onesie sits upright inside a simple wooden crib, facing the viewer with an upright, level face and a curious expression, looking up; two small adult hands, each no bigger than the baby's head and in correct proportion to the crib, reach in from the top edge of the frame, one holding a small pink paint swatch and the other a small baby blue paint swatch. The baby's face has two perfectly round eyes of exactly the same size side by side, a tiny nose and one small mouth.",anim="The two giant hands slowly lower the pink and blue swatches toward the baby, who blinks up at them.")

C='Title'
s(C,"The Color You Were Told to Wear.","Title background on plain off-white: a tipped-over can of soft pastel pink paint on the left and a tipped-over can of baby blue paint on the right, the two paint puddles flowing toward each other and meeting in the middle; empty space across the top for a title added later.",anim="The pink and blue paint slowly spread across the floor until the two puddles touch in the center.")

C='Everyone in white'
s(C,"Go back to the eighteen hundreds and look at a family photo.","Wide shot in an 1880s photo studio with a painted backdrop: the Victorian mother, a Victorian father in a dark brown suit with short brown hair, and three small children pose stiffly on a bench while a photographer stands behind a wooden box camera on a tripod under a dark cloth.",'VB',True)
s(C,"Every small child is in a white dress.","Medium shot: three Victorian toddlers sit in a row on a velvet bench, all in identical knee-length cream baby dresses with lace hems; one has brown curls, one has blonde curls, one has auburn hair.",'B',True)
s(C,"The girls, yes.","Close-up: two Victorian toddler girls in cream lace dresses with small cream hair bows, one with blonde curls and one with auburn hair, looking at the viewer.",'',True)
s(C,"The boys too.","Close-up: the Victorian toddler boy in his cream lace dress holds a small wooden toy horse, looking at the viewer with a calm deadpan face.",'B')
s(C,"There's a famous photo of a two year old Franklin Roosevelt in a white dress, long hair, and a feathered hat,","Medium shot styled like an old portrait inside a simple oval frame: a two-year-old boy with long light brown curls sits on a tall stool, wearing a cream lace dress and a wide brimmed cream hat with one big dusty blue feather.",anim="The feather on the toddler's hat sways gently and the toddler swings his little legs.")
s(C,"and in his time nobody would have blinked.","Medium shot in a Victorian parlor: the Victorian mother and a Victorian father in a dark brown suit look down at the same toddler in his cream dress and feathered hat with calm approving smiles.",'V',True)
s(C,"White was practical.","Close-up: a neat stack of folded cream baby dresses on a plain wooden table, a small cake of soap beside them.")
s(C,"Babies are messy,","Medium shot: the Victorian toddler boy sits at a small table, his cream dress smeared with brown porridge, a tipped wooden bowl in front of him, grinning happily.",'B')
s(C,"and white cotton could be boiled and bleached until it looked new again.","Medium shot in a Victorian kitchen: the Victorian mother stirs a big copper pot of boiling cream laundry over a stove with a long wooden stick, puffs of steam rising.",'V',anim="The mother stirs the pot in slow circles while steam rises and curls upward.")
s(C,"A dress was easy to change, easy to let out as the child grew,","Close-up: the Victorian mother sits in a chair letting out the hem of a small cream baby dress with needle and thread, an open wicker sewing basket beside her.",'V')
s(C,"and easy to pass down from one child to the next, no matter who came next.","Wide shot against a sage green wall: four Victorian siblings stand in a row from tallest to smallest, the tallest girl handing a folded cream baby dress down the line toward the smallest, the Victorian toddler boy, at the end.",'B',True,anim="The folded cream dress is passed from hand to hand down the line until the smallest boy receives it and smiles.")
s(C,"Boys only got their first trousers at around six or seven.","Medium shot: a Victorian boy of about six with short brown hair stands proudly in a brand-new brown knee-length trouser suit with a cream collar, chest puffed out.")
s(C,"It was a big day, almost a ceremony, with a haircut and a new suit.","Medium shot in a Victorian barbershop: a barber in a striped vest cuts long brown curls off a six-year-old boy sitting on a tall chair, curls falling to the floor, the Victorian mother watching proudly.",'V',True)
s(C,"Until then, a baby was just a baby.","Close-up: a sleeping baby in a cream gown lies in a woven wicker cradle against a plain periwinkle wall, peaceful.")
s(C,"Pastel colors did show up in the middle of the century, pink and blue among them.","Medium shot inside a Victorian fabric shop: wooden shelves of fabric bolts in soft pastel pink, baby blue, sage green, lavender and pale yellow.")
s(C,"But they were decoration, not a rule.","Close-up on off-white: a cream baby dress decorated with a small pastel pink ribbon sash and a small baby blue ribbon on the matching bonnet, both on the same outfit.")
s(C,"A little pink ribbon said nothing about who was wearing it.","Medium shot: the Victorian toddler boy in his cream dress wears a small pink ribbon in his curls and shrugs at the viewer, a small amber question mark beside him.",'B')

C='Pink is for boys'
s(C,"Then, in June nineteen eighteen, a trade magazine called Infant's Department told store owners what the accepted rule was.","Medium shot in a 1918 baby-clothes shop: the 1918 baby-store owner leans on the counter reading a magazine whose cover reads \"INFANT'S DEPARTMENT\"; small baby clothes hang on a rack behind him.",'K',anim="The man turns a page of the magazine, pauses and raises his eyebrows.")
s(C,"Pink for the boy, blue for the girl.","Infographic on off-white: a 1918 toddler boy with short brown hair in a soft pastel pink romper stands on the left, and a 1918 toddler girl with auburn curls in a baby blue dress stands on the right, both facing the viewer.")
s(C,"And it gave a reason.","Close-up: the 1918 baby-store owner taps an open magazine page full of gray scribble lines with one finger, leaning toward the viewer.",'K')
s(C,"Pink, it said, is a more decided and stronger color, so it suits a boy.","Medium shot on a plain pink wall: a 1918 toddler boy with short brown hair in a soft pastel pink romper proudly lifts a tiny toy wooden barbell over his head like a circus strongman.",anim="The toddler boy lifts the tiny barbell up and down twice with a proud face.")
s(C,"Blue is more delicate and dainty, so it's prettier for a girl.","Medium shot on a plain baby blue wall: a 1918 toddler girl with auburn curls in a baby blue dress delicately holds a single daisy and a tiny teacup, pinky finger raised.")
s(C,"Think about that.","Close-up: the 1918 baby-store owner gives the viewer a slow deadpan side glance over his spectacles.",'K')
s(C,"The same logic people use today, strong versus delicate, was used to argue the exact opposite.","Infographic on off-white: an old brass balance scale; on one pan a pink block with the word \"STRONG\", on the other pan a baby blue feather with the word \"DELICATE\".")
s(C,"Pink was seen as a lighter shade of red, the color of soldiers' coats and fighting spirit.","Medium shot on off-white: a painter's palette where a bright dusty red blob is being mixed with white into pink by a brush; behind it a toy-like soldier in an old-fashioned red coat marches.")
s(C,"Blue, some said, was the color of calm and of the Virgin Mary.","Medium shot: a simple arched church stained glass window in calm blue tones showing a gentle robed woman in a long blue veil with a complete face, hands folded.")
s(C,"The colors didn't carry meaning.","Close-up on plain off-white: one pink paint swatch and one baby blue paint swatch float side by side, empty and plain.")
s(C,"The meaning was attached to them, by whoever was selling.","Medium shot: the 1918 baby-store owner pins small paper tags onto a big pink swatch and a big blue swatch with a sly little smile.",'K',anim="The man pins a paper tag onto the pink swatch, then onto the blue swatch, and smiles slyly at the viewer.")

C='Nobody agreed'
s(C,"And sellers did not agree.","Medium shot: two 1920s shopkeepers face each other across a counter, arguing; one with black hair holds up a pink romper, the other with gray hair holds up a baby blue romper; no other people in the shop. Every face has two perfectly round eyes of exactly the same size, both looking in the same direction.",'',True)
s(C,"In nineteen twenty seven, Time magazine asked the biggest department stores in America which color was for which child.","Medium shot in a 1927 newsroom: a reporter with short brown hair, a vest and sleeve garters talks into a candlestick telephone while writing on a notepad; a map of the United States hangs on the wall; no other people in the room. Every face has two perfectly round eyes of exactly the same size, both looking in the same direction.",'',True)
s(C,"Filene's in Boston said pink for boys.","Infographic: a simple flat map of the eastern United States on off-white; a pink pin in Boston with a tiny toddler boy icon beside it and the label \"BOSTON\".")
s(C,"So did Marshall Field's in Chicago, Best and Company in New York, and Halle Brothers in Cleveland.","Infographic: the same flat map of the eastern United States; pink pins in Chicago, New York and Cleveland, each with a tiny toddler boy icon.",anim="Pink pins pop up one after another on Chicago, New York and Cleveland.")
s(C,"Other stores said the opposite.","Infographic: a simple flat map of the eastern United States only (not the world) on off-white, with three pink pins and four baby blue pins scattered over different cities, each pin with a tiny toddler boy icon.")
s(C,"Imagine being a new parent in nineteen twenty seven.","Wide shot: the 1927 young mother holds a baby wrapped in a cream blanket in front of a grand 1920s department store with big display windows, shoppers in 1920s clothes passing by.",'M',True)
s(C,"You buy a pink outfit for your son in Chicago,","Medium shot inside a 1920s store: the 1927 young mother pays at the counter while a clerk wraps a soft pastel pink baby romper in brown paper.",'M',True)
s(C,"visit your sister in another city,","Medium shot on a 1920s train platform: the 1927 young mother with a small suitcase and a baby steps off a train, her sister with an auburn bob and a sage green coat waves to greet her.",'M',True)
s(C,"and her local store tells you that you got it backwards.","Medium shot inside another 1920s store: a clerk with gray hair shakes his head and points at a baby blue romper, while the 1927 young mother holds up the pink romper, embarrassed.",'M',True,anim="The clerk shakes his head and points at the blue romper; the mother slowly lowers the pink romper, embarrassed.")
s(C,"Historians still argue about how common each version was.","Medium shot in a library: two historians, a man with gray hair and glasses and a woman with a black bun, stand beside a tall stack of old newspapers, pointing at each other mid-argument.",'',True)
s(C,"One study of old newspapers found both versions printed side by side for decades.","Close-up: two yellowed old newspaper clippings lie side by side, each with gray scribble lines; one shows a small pink swatch beside a boy icon, the other a small baby blue swatch beside a boy icon.")
s(C,"The honest answer is that there was no rule.","Medium shot: the 1927 young mother stands between two store doors, one pink and one blue, holding her baby and shrugging.",'M')
s(C,"There were stores, and each store had a guess.","Wide shot of a quiet 1920s shopping street with four storefronts side by side and no passersby; in each doorway stands one shopkeeper holding up a big colored swatch (pink, baby blue, pale yellow, sage green), with a small amber question mark above each shopkeeper.",'',True)

C='The rule arrives'
s(C,"Somewhere in the middle of the twentieth century, the guesses settled.","Infographic on off-white: a horizontal timeline from \"1920\" to \"1950\"; small pink and blue swatches tumble and spin along it and land neatly in two separate piles at the end.")
s(C,"Pink went to girls.","Medium shot: a 1950s baby girl in a pastel pink bonnet and pink knit jacket sits in a big rounded 1950s pram.")
s(C,"Blue went to boys.","Medium shot: a 1950s baby boy in a baby blue romper sits in a wooden high chair holding a rattle.")
s(C,"No law was passed.","Close-up: an old rubber stamp marked \"LAW\" lies unused next to a dry ink pad on a dusty desk, a small cobweb between them.")
s(C,"No scientist proved anything.","Medium shot: a 1950s scientist with black hair and a white lab coat over a slate blue shirt peers into a microscope at a pink swatch, then shrugs with a puzzled face.")
s(C,"Manufacturers and stores simply kept repeating the same pairing until it felt like nature.","Wide shot in a 1950s factory: a long conveyor belt carries plain cream baby clothes under two big machines that stamp them pink on one side and baby blue on the other, workers in caps watching.",'',True,anim="The conveyor belt moves steadily; the machines stamp the clothes pink and blue one after another.")
s(C,"In the nineteen fifties, pink became the color of grown up femininity too.","Medium shot in a pastel 1950s kitchen: the 1950s mother in her pink dress stands proudly beside a rounded pink refrigerator.",'R')
s(C,"When Mamie Eisenhower wore a pink gown to her husband's inauguration in nineteen fifty three,","Medium shot at a 1953 inaugural ball: the First Lady, recognizable by her short curly brown bangs, in a full-skirted pale pink ball gown dotted with tiny sparkles, waves gracefully; couples in evening wear in the background.",'',True,anim="The woman waves slowly and the tiny sparkles on her pink gown twinkle.")
s(C,"the press loved it,","Medium shot: a row of 1950s press photographers in hats raise big flash cameras, bright flashes drawn as amber starbursts.",'',True)
s(C,"and soon there were pink kitchens, pink bathrooms, and pink appliances in American homes.","Wide cutaway of a 1950s house like a dollhouse: a pink kitchen, a pink-tiled bathroom, a pink fridge and a pink mixer, the 1950s mother dusting in one room.",'R')
s(C,"The baby boom generation grew up color coded from the crib.","Medium shot in a 1950s nursery: two cribs side by side, one painted pink with a baby girl, one painted baby blue with a baby boy.")
s(C,"Boys in blue, girls in pink,","Wide shot: a 1950s school class photo on bleachers, all boys in baby blue shirts and all girls in pink dresses, varied hair colors.",'',True)
s(C,"and every relative knew exactly what gift to bring.","Medium shot: the 1950s mother opens her front door to smiling grandparents holding gift boxes wrapped in pink and in baby blue.",'R',True)

C='The pause'
s(C,"Then something strange happened.","Close-up: the 1970s mother in a 1970s living room with an orange-brown sofa raises one eyebrow at the viewer.",'S')
s(C,"In the late sixties and seventies, many parents rejected it.","Medium shot in a 1970s children's store: the 1970s mother holds up one hand politely refusing a frilly pink dress offered by a saleswoman with blonde hair.",'S',True)
s(C,"The women's movement pushed back against the idea that girls had to look soft and sweet.","Wide shot: a peaceful 1970s march of women in flared jeans and turtlenecks carrying simple placards with neat gray scribble lines, one reading \"EQUAL\".",'',True)
s(C,"Unisex clothes took over.","Medium shot: the 1970s toddler and a second toddler with black hair stand side by side in identical striped shirts and denim overalls; you cannot tell which is the boy and which is the girl.",'T')
s(C,"Overalls, stripes, red, yellow, green.","Flat lay from above on off-white: small denim overalls, a dusty red and yellow striped shirt, a sage green corduroy jacket and a mustard knit cap.")
s(C,"Reportedly, for two whole years in the seventies, the Sears catalog didn't show a single pink toddler outfit.","Close-up: a thick open 1970s mail-order catalog with pages of children's clothes in yellow, green, brown and orange; a magnifying glass hovers over the pages searching.",anim="The catalog pages flip one after another while the magnifying glass searches in vain.")
s(C,"For a moment, it looked like the rule was dying,","Close-up: a pink flower in a small pot wilting and drooping, petals falling, on a plain off-white background.")
s(C,"and that kids might go back to being just kids.","Medium shot: the 1970s toddler and another toddler play happily in a sandbox in neutral overalls, building a sandcastle.",'T',True)

C='The sonogram sale'
s(C,"It wasn't dying.","Close-up: the same pink flower in its pot suddenly springs back up, bright and tall, more pink than ever.",anim="The wilted pink flower springs upright and blooms bigger and pinker.")
s(C,"In the nineteen eighties, prenatal tests became common,","Medium shot in a 1980s clinic: the 1980s mother lies on an exam bed while a doctor with gray hair looks at a boxy ultrasound monitor showing a simple gray blob; the 1980s father holds her hand.",'WD')
s(C,"and parents could learn whether it was a boy or a girl months before the birth.","Medium shot: the 1980s mother and father look at each other excitedly, with two thought bubbles above them, one pink and one baby blue.",'WD')
s(C,"That gave stores something new to sell:","Medium shot: a 1980s store manager with a brown mullet and a wide tie rubs his hands together behind a cash register.")
s(C,"time.","Close-up: a big wall calendar with months crossed off one by one toward a circled date with an amber star, small shopping bags piling up beneath it.")
s(C,"Now you could shop for a specific kind of baby before it arrived.","Wide shot in a 1980s baby store: the pregnant 1980s mother and the 1980s father push a shopping cart overflowing with pink baby items, other shoppers in the aisles.",'WD',True)
s(C,"And the industry noticed.","Medium shot in a 1980s boardroom: executives in shoulder-padded suits look at a chart on an easel with tall pink and baby blue bars rising.",'',True)
s(C,"Neutral clothes started to disappear.","Medium shot: a clothing rack of pale yellow and sage green baby clothes fading into thin dotted outlines, as if vanishing.")
s(C,"A plain blue romper suddenly had a little football on it.","Close-up on off-white: a baby blue romper with a small brown football patch sewn on the chest.")
s(C,"A plain pink one got a bow and a kitten.","Close-up on off-white: a soft pastel pink romper with a small bow and a cute kitten patch on the chest.")
s(C,"And pink spread far beyond clothes.","Wide shot: a wave of soft pink paint washes across the floor of a store, coloring everything it touches.")
s(C,"Strollers. Car seats.","Medium shot on off-white: a pastel pink stroller and a pastel pink baby car seat side by side.")
s(C,"Bottles. Bedding. Wallpaper.","Wide shot of a 1980s nursery: pink baby bottles on a shelf, pink bedding in the crib and pink wallpaper with tiny hearts.")
s(C,"Historian Jo Paoletti put the logic in one line.","Medium shot: a historian woman with a short gray bob, round glasses and a dusty blue blazer stands at a lectern holding an open book.")
s(C,"The more you individualize clothing, the more you can sell.","Infographic on off-white: one plain cream baby onesie splits into two (one pink, one baby blue), then into four, with a pile of gold coins growing beside them.",anim="The single onesie splits into two, then four, while the stack of gold coins grows taller.")

C='Pink everything'
s(C,"By the two thousands, the split covered almost everything a child could touch.","Wide shot: a big bright modern toy store with high shelves, families shopping.",'',True)
s(C,"Toy stores had a pink aisle and a blue aisle.","Wide shot looking down two aisles: the left aisle has only pink shelves and toys, the right aisle only blue; the modern girl walks into the pink aisle and the modern boy into the blue aisle.",'GL',True)
s(C,"Building bricks got a separate pink line for girls.","Close-up on off-white: a box of pastel pink and lavender toy building bricks next to a box of gray and blue toy building bricks, no logos.")
s(C,"And it didn't stop at childhood.","Medium shot in a drugstore aisle: the modern woman looks at shelves where every product comes in a pink version and a blue version.",'H')
s(C,"In twenty fifteen, a New York City study compared nearly eight hundred products sold in a men's and a women's version.","Wide shot: a researcher with black hair and a cream cardigan stands at a long table covered with pairs of identical products, one pink and one blue each, checking them off on a clipboard.")
s(C,"On average, the women's version cost about seven percent more,","Close-up on off-white: two identical razors side by side, one baby blue with a small price tag, one pink with a bigger price tag marked \"+7%\".")
s(C,"often for the same item in a different color.","Close-up on off-white: two identical kids' scooters, one pink and one baby blue, the pink one with a bigger price tag.")
s(C,"People started calling it the pink tax.","Close-up: a long store receipt with gray scribble lines and a big pink stamp across it reading \"PINK TAX\".")
s(C,"Then, in two thousand eight, an American mother cut into a cake at a party to reveal pink frosting inside,","Medium shot at a 2008 party: a pregnant woman with wavy honey-brown hair and a cream cardigan cuts into a white frosted cake; the slice reveals bright pink inside; guests gasp and clap.",'',True,anim="The woman lifts a slice of cake to reveal pink inside and the guests clap.")
s(C,"and posted about it online.","Close-up: the same woman types on a chunky 2008 laptop; the screen shows a simple blog page with a photo of the pink cake and gray scribble lines.")
s(C,"The gender reveal party was born.","Medium shot: a backyard decorated with bunches of pink and baby blue balloons and an empty bunting banner, a cake table in the middle.")
s(C,"Today it's a whole industry of balloons, smoke cannons and confetti,","Wide shot in a modern backyard: a young couple pops a giant black balloon that bursts into pink confetti while a smoke cannon puffs a cloud of pink smoke; guests cheer.",'',True,anim="The giant balloon bursts and pink confetti rains down while pink smoke billows up and the guests cheer.")
s(C,"all built on one question: pink or blue?","Close-up on off-white: two big round buttons, one pink and one baby blue, with a hand-drawn finger hovering between them.")

C='Why it still works'
s(C,"Here's the quiet genius of it.","Close-up: the modern woman looks at the viewer with a small knowing raised eyebrow.",'H')
s(C,"A white dress could go from a big sister to a little brother.","Medium shot in a Victorian parlor: a Victorian girl of about six with brown braids hands a folded cream baby dress to the Victorian toddler boy, who smiles.",'B')
s(C,"A pink stroller can't.","Medium shot in a modern hallway: the modern woman holds her baby son in a baby blue onesie and looks at an old pastel pink stroller standing by the wall, hesitating.",'H')
s(C,"Not easily, anyway.","Close-up: the modern woman shrugs with a half smile, the pink stroller beside her.",'H')
s(C,"Most parents feel a small pinch of awkwardness pushing their son in something bright pink,","Medium shot in a modern park: a modern dad with short brown hair and a sage green jacket pushes a baby boy in a bright pink stroller; two passersby on a bench glance at it.",'',True,anim="The dad pushes the pink stroller along the path and glances sideways at the passersby with an awkward smile.")
s(C,"and that small pinch is enough.","Close-up: the modern dad's face with a stiff awkward smile and a single small sweat drop.")
s(C,"A second child of the other sex now means a second set of everything.","Wide shot in a modern garage: two identical piles of baby gear, one all pink and one all baby blue (stroller, car seat, crib, clothes), the modern woman standing between them.",'H')
s(C,"Nobody ever told you to buy twice.","Medium shot at a store checkout: the modern woman unloads a cart full of baby blue baby items while a very long receipt curls onto the floor.",'H',True)
s(C,"They just painted the first set a color that made reusing it feel wrong.","Close-up: a hand-drawn hand with a paintbrush painting a plain cream stroller pastel pink, a little paint dripping.")
s(C,"And the rule teaches itself.","Medium shot on a pale butter yellow wall: the modern boy and the modern girl stand side by side looking at each other's toys, the girl holding a pink doll and the boy a blue toy truck.",'LG')
s(C,"Kids learn it from the aisles, from the gifts, from the cake.","Triptych in three equal panels: a pink and blue toy aisle; a pile of gifts wrapped in pink and blue; a slice of cake with pink inside.")
s(C,"By the age of four, many of them will police it for you.","Medium shot in a preschool: the modern boy points at another little boy with red hair holding a pink cup and shakes his head disapprovingly.",'L',True)
s(C,"Every time a store builds a pink aisle and a blue aisle, the rule gets taught again,","Medium-wide shot of a store at night with dim lights: two workers in vests, a man with brown hair and a woman with black hair, stack toys onto all-pink shelves in one aisle and all-blue shelves in the next; no other people. Every face has two perfectly round eyes of exactly the same size, both looking in the same direction.",'',True)
s(C,"to a new set of parents who think they're choosing freely.","Medium shot: the modern woman and her husband, a man with short brown hair, a trimmed brown beard and a sage green sweater, stand at a clothing rack holding up a small pink baby outfit with happy smiles; very thin faint gray puppet strings run from their wrists up out of the top of the frame to a cartoon hand. Every face has two perfectly round eyes of exactly the same size, both looking in the same direction.",'H',True)

C='Ending'
s(C,"A hundred years ago, a magazine told parents that pink was strong enough for a boy.","Medium shot, callback to the opening: the 1918 baby-store owner behind his counter holds up the open magazine to the viewer, a small pink romper on the counter.",'K')
s(C,"Today, the same color is supposed to be too soft for him.","Medium shot in a modern kitchen: the modern boy pushes away a pink cup across the table with a frown, reaching for a blue one.",'L')
s(C,"The color never changed.","Close-up on plain off-white: a single soft pastel pink paint swatch in the center of the frame.")
s(C,"Only the story around it did.","Close-up on plain off-white: the same pink swatch surrounded by small paper tags with gray scribble lines circling around it.",anim="The paper tags swirl slowly around the pink swatch like orbiting planets.")
s(C,"So the next time someone asks, is it a boy or a girl,","Medium shot at a modern baby shower: the pregnant modern woman talks with a smiling guest with curly black hair who asks her a question, a speech bubble with a pink and a blue dot.",'H',True)
s(C,"notice what the question really means:","Close-up: the modern woman's face as she pauses and realizes something, eyes slightly wider.",'H')
s(C,"which aisle are we shopping in?","Wide symmetrical shot: the modern woman stands small at the exact point where an all-pink store aisle and an all-blue store aisle split, looking from one to the other.",'H',anim="The modern woman slowly looks left at the pink aisle, then right at the blue aisle, as the store lights hum.")
s(C,"Made to Want.","End card on plain off-white: the words \"MADE TO WANT\" in clean bold hand-drawn capitals in the center, with one small pink swatch and one small baby blue swatch beneath.")

# ---------- checks ----------
txt = open(SCRIPT, encoding='utf-8').read()
chap_txt = {}
for part in re.split(r'\n## ', txt)[1:]:
    head, body = part.split('\n', 1)
    chap_txt[re.sub(r'^\d+\.\s*', '', head).strip()] = ' '.join(body.split())
order = []
for x in S:
    if x['chapter'] not in order: order.append(x['chapter'])
norm = lambda t: ' '.join(t.split())
for c in order:
    joined = norm(' '.join(x['vo'] for x in S if x['chapter'] == c))
    assert joined == chap_txt[c], f'VO mismatch in {c}:\n{joined}\n---\n{chap_txt[c]}'

# keep animation budget ~15 clips: these stay stills (smoothzoom)
DROP_ANIM = ("and white cotton could be boiled", "Then, in June nineteen eighteen", "So did Marshall Field's",
             "Manufacturers and stores simply", "Reportedly, for two whole years", "Only the story around it did.")
for x in S:
    if x['vo'].startswith(DROP_ANIM): x['anim'] = ''

# shots with uncarded people that also need the channel face/style rule
PEOPLE_EXTRA = {6,7,13,20,22,27,29,30,33,51,52,54,60,72,74,84,90,95,100,101,104}
shots = []
for i, x in enumerate(S, 1):
    parts = [x['scene']] + [CHARS[k]['desc'] for k in x['chars']]
    if x['crowd'] or i in PEOPLE_EXTRA: parts.append(CROWD)
    parts.append(STYLE)
    shots.append(dict(n=i, chapter=x['chapter'], vo=x['vo'], scene=x['scene'], chars=x['chars'], anim=x['anim'], prompt=' '.join(parts)))

json.dump(dict(style=STYLE, crowd=CROWD, chars={k: v['desc'] for k, v in CHARS.items()}, shots=shots),
          open(os.path.join(HERE, 'storyboard.json'), 'w'), ensure_ascii=False, indent=1)
SHEET = 'Character model sheet for an animated explainer channel: the same single character shown twice side by side on a plain off-white background, front view and three-quarter view, standing in a relaxed neutral pose, same size, feet on one thin ground line. '
cards = [dict(key=k, name=v['name'], prompt=SHEET + v['desc'] + ' No text, no labels. ' + STYLE) for k, v in CHARS.items()]
json.dump(cards, open(os.path.join(HERE, 'char_cards.json'), 'w'), ensure_ascii=False, indent=1)
with open(os.path.join(HERE, 'vo_chapters.txt'), 'w', encoding='utf-8') as f:
    for c in order: f.write(chap_txt[c] + '\n')
words = sum(len(chap_txt[c].split()) for c in order)
print(len(shots), 'shots;', sum(1 for x in shots if x['anim']), 'anims;', words, 'words ≈', round(words/155, 1), 'min')
