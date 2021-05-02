import json

str_json =  """
{
		"response": {
			"items" : [
			{
				"kz" : "анофелдер",
				"ru" : "анофелес",
				"en" : "anopheles",
				"kz-def" : "Безгек паразиттерінің екіншілік иелері болып табылатын және тістеуі адамдарға безгекті жұқтыратын қарапайым, тіпті жалғыз құрал болып табылатын масалардың бір түрі. Бірнеше түрі АҚШ-та кездеседі. Оларды Culex тектес қарапайым масалардан тұмсық ұзындығына тең болатын ұзын, жіңішке пальпалары арқылы ажыратуға болады, ал аналықтарда аналықтар өте қысқа. Олар демалу кезінде де әртүрлі позицияларды алады: Кюлекс әдетте денені жатқан бетіне параллель ұстайды және басын және тұмсықты бұрышпен бүгеді, ал Анофелес денені бетке және бас пен тұмсықты бір бұрышта ұстайды . осымен. Егер олар алдымен ауруды безгегімен шағу арқылы жұқпаса, жәндіктер ауруды жұқтыра алмайды.",
				"ru-def" : "Род комаров, которые являются вторичными хозяевами малярийных паразитов и укус которых является обычным, если не единственным, средством заражения людей малярией. Несколько видов обитают в Соединенных Штатах. Их можно отличить от обычных комаров рода Culex по длинным тонким щупикам, почти равным длине клюва, тогда как у самок Culex они очень короткие. Они также принимают разные положения во время отдыха: Culex обычно держит тело параллельно поверхности, на которой он лежит, и держит голову и клюв согнутыми под углом, в то время как Anopheles держит тело под углом к поверхности, а голову и клюв на одной линии. . с этим. Если они не заразятся, сначала укусив больного малярией, насекомые не могут передать болезнь.",
				"en-def" : "A genus of mosquitoes which are secondary hosts of the malaria parasites, and whose bite is the usual, if not the only, means of infecting human beings with malaria. Several species are found in the United States. They may be distinguished from the ordinary mosquitoes of the genus Culex by the long slender palpi, nearly equaling the beak in length, while those of the female Culex are very short. They also assume different positions when resting, Culex usually holding the body parallel to the surface on which it rests and keeping the head and beak bent at an angle, while Anopheles holds the body at an angle with the surface and the head and beak in line with it. Unless they become themselves infected by previously biting a subject affected with malaria, the insects cannot transmit the disease."
			},
			{
				"kz" : "саронг",
				"ru" : "саронг",
				"en" : "sarong",
				"kz-def" : "Ява мен Малай архипелагындағы екі жыныс киетін петухаттың бір түрі. Бальфур (Үндістан циклі)",
				"ru-def" : "Что-то вроде юбки, которую носят представители обоих полов на Яве и Малайском архипелаге. Бальфур (Cyc. Of India)",
				"en-def" : "A sort of petticoat worn by both sexes in Java and the Malay Archipelago. Balfour (Cyc. of India)"
			},
			{
				"kz" : "түрікмен",
				"ru" : "туркмен",
				"en" : "turcoman",
				"kz-def" : "Каспий теңізінің шығысында орналасқан аймақты мекендеген турандықтар тайпасының мүшесі.",
				"ru-def" : "Член племени туранцев, населяющих регион к востоку от Каспийского моря.",
				"en-def" : "A member of a tribe of Turanians inhabiting a region east of the Caspian Sea. "
			},
			{
				"kz" : "гофр",
				"ru" : "гофроагрегат",
				"en" : "corrugator",
				"kz-def" : "Маңдай терісін әжімдерге қысатын бұлшықет.",
				"ru-def" : "Мышца, которая сокращает кожу лба до морщин.",
				"en-def" : "A muscle which contracts the skin of the forehead into wrinkles."
			},
			{
				"kz" : "өзін-өзі өлтіру",
				"ru" : "самоубийство",
				"en" : "self-murder",
				"kz-def" : "Суицид.",
				"ru-def" : "Самоубийство.",
				"en-def" : "Suicide."
			},
			{
				"kz" : "анакардия",
				"ru" : "анакард",
				"en" : "anacardium",
				"kz-def" : "Кешью ағашын қосатын өсімдіктер тұқымдасы. Кешьюді қараңыз.",
				"ru-def" : "Род растений, в том числе дерево кешью. См. Кешью.",
				"en-def" : "A genus of plants including the cashew tree. See Cashew."
			},
			{
				"kz" : "шын жүректен",
				"ru" : "сучковатый",
				"en" : "knurly",
				"kz-def" : "Түйіндерге толы; қатты; қатал; демек, көп нәрсеге төзуге немесе қарсы тұруға қабілетті.",
				"ru-def" : "Полный узлов; жесткий; жесткий; следовательно, способен вынести или сопротивляться многому.",
				"en-def" : "Full of knots; hard; tough; hence, capable of enduring or resisting much."
			},
			{
				"kz" : "қалта",
				"ru" : "рвануть",
				"en" : "pock",
				"kz-def" : "Вариолды және вакцина аурулары кезінде дененің бетінде көтерілген пустула. Поккелер мен қотырлар. Чосер.",
				"ru-def" : "Пустула, возвышающаяся на поверхности тела при различных и вакцинных заболеваниях. Поккес и корка всякой болячки. Чосер.",
				"en-def" : "A pustule raised on the surface of the body in variolous and vaccine diseases. Of pokkes and of scab every sore. Chaucer."
			},
			{
				"kz" : "нейрома",
				"ru" : "неврома",
				"en" : "neuroma",
				"kz-def" : "Esp, жүйкеде дамыған немесе олармен байланысты ісік. жаңа пайда болған жүйке талшықтарынан тұрады.",
				"ru-def" : "Опухоль развивалась на нерве или связана с ним, особенно. один, состоящий из новообразованных нервных волокон.",
				"en-def" : "A tumor developed on, or connected with, a nerve, esp. one consisting of new-formed nerve fibers."
			},
			{
				"kz" : "қарақұйрық",
				"ru" : "трос",
				"en" : "hawser",
				"kz-def" : "Әрқайсысында көптеген иірілген жіптер бар үш жіптен жасалған үлкен арқан. Ескерту: бір-біріне бұралған үш лақтырғыш кабель жасайды; бірақ теңізде қолдану үшін кабель мен сатушы арасындағы айырмашылық көбінесе өндіріске емес, өлшемге байланысты болады. Хаусер темірі, тыныштандыратын темір.",
				"ru-def" : "Большая веревка, состоящая из трех нитей, каждая из которых состоит из множества нитей. Примечание: три троса, скрученные вместе, образуют трос; но в мореплавании различие между канатом и тросом часто определяется размером, а не производством. Утюг Hawser, утюг для кальцинирования.",
				"en-def" : "A large rope made of three strands each containing many yarns. Note: Three hawsers twisted together make a cable; but it nautical usage the distinction between cable and hawser is often one of size rather than of manufacture. Hawser iron, a calking iron."
			},
			{
				"kz" : "қуанышты",
				"ru" : "трясущийся",
				"en" : "jolty",
				"kz-def" : "Сол сілкіністер; ретінде, көңілді жаттықтырушы.",
				"ru-def" : "Это потрясает; как трясущийся тренер.",
				"en-def" : "That jolts; as, a jolty coach."
			},
			{
				"kz" : "лейцикалық",
				"ru" : "лейциновый",
				"en" : "leucic",
				"kz-def" : "Лейциннен алынған, сондай-ақ окси-капрой қышқылы деп аталатын қышқылға жатады немесе белгіленеді.",
				"ru-def" : "Относится к кислоте, полученной из лейцина, или обозначает кислоту, также называемую оксикапроновой кислотой.",
				"en-def" : "Pertaining to, or designating, an acid obtained from leucine, and called also oxy caproic acid."
			},
			{
				"kz" : "петресценция",
				"ru" : "каменистость",
				"en" : "petrescence",
				"kz-def" : "Тасқа айналу процесі; тасқа айналу.",
				"ru-def" : "Процесс превращения в камень; окаменение.",
				"en-def" : "The process of changing into stone; petrification."
			},
			{
				"kz" : "батос",
				"ru" : "батос",
				"en" : "bathos",
				"kz-def" : "Жазбаша немесе сөйлеу кезінде жоғарыдан төменге қарай күлкілі түсу; антиклимакс.",
				"ru-def" : "Нелепое падение от возвышенного к низшему в письменной или устной форме; успокаивающий.",
				"en-def" : "A ludicrous descent from the elevated to the low, in writing or speech; anticlimax."
			},
			{
				"kz" : "бейнелеу",
				"ru" : "облектация",
				"en" : "oblectation",
				"kz-def" : "Көңілге қонымды әрекет; өте риза болған жағдай; қуаныш.",
				"ru-def" : "Акт удовольствия в высшей степени; состояние очень довольного; восторг.",
				"en-def" : "The act of pleasing highly; the state of being greatly pleased; delight."
			},
			{
				"kz" : "басып озу",
				"ru" : "протекать",
				"en" : "overtread",
				"kz-def" : "Үстінен немесе үстінен басу.",
				"ru-def" : "Наступить или наступить.",
				"en-def" : "To tread over or upon."
			},
			{
				"kz" : "блейзер",
				"ru" : "блейзер",
				"en" : "blazer",
				"kz-def" : "Шет елдерде есептер тарататын немесе жалындаған адам.",
				"ru-def" : "Тот, кто распространяет репортажи или разжигает заграничные дела.",
				"en-def" : "One who spreads reports or blazes matters abroad."
			},
			{
				"kz" : "элегист",
				"ru" : "элегист",
				"en" : "elegist",
				"kz-def" : "Элегия жазуы.",
				"ru-def" : "Написание элегий.",
				"en-def" : "A write of elegies."
			},
			{
				"kz" : "қастандық жасаушы",
				"ru" : "заговорщик",
				"en" : "conspirator",
				"kz-def" : "Қастандық жасаушы; плоттер.",
				"ru-def" : "Тот, кто участвует в заговоре; плоттер.",
				"en-def" : "One who engages in a conspiracy; a plotter."
			},
			{
				"kz" : "хинзе",
				"ru" : "ангина",
				"en" : "quinze",
				"kz-def" : "Он бес ұпай жинауға арналған карточкалардағы ойын.",
				"ru-def" : "Игра в карты, цель которой - набрать пятнадцать очков.",
				"en-def" : "A game at cards in which the object is to make fifteen points."
			},
			{
				"kz" : "тарату",
				"ru" : "скрывать",
				"en" : "dissimulate",
				"kz-def" : "Фигуралау; модельдеу; кейіп таныту.",
				"ru-def" : "Симулирование; моделирование; притворяется.",
				"en-def" : "Feigning; simulating; pretending."
			},
			{
				"kz" : "қарасора",
				"ru" : "конопля",
				"en" : "hempen",
				"kz-def" : "Қарасорадан жасалған; сияқты, қарақұйрық сымы.",
				"ru-def" : "Изготовлен из конопли; как, пеньковый шнур.",
				"en-def" : "Made of hemp; as, a hempen cord."
			},
			{
				"kz" : "тимпанист",
				"ru" : "тимпанист",
				"en" : "tympanist",
				"kz-def" : "Барабанды ұратын адам.",
				"ru-def" : "Тот, кто бьет в барабан.",
				"en-def" : "One who beats a drum."
			},
			{
				"kz" : "ескі",
				"ru" : "старомодный",
				"en" : "old-fashioned",
				"kz-def" : "Ескі немесе ескірген сәнге немесе үлгіге сәйкес қалыптасады; ескі әдет-ғұрыптарды немесе идеяларды ұстану; сияқты, ескі көйлек, қыз.",
				"ru-def" : "Формируется по старой или устаревшей моде или образцу; соблюдение старых обычаев или идей; как, старомодное платье, девочка.",
				"en-def" : "Formed according to old or obsolete fashion or pattern; adhering to old customs or ideas; as, an old-fashioned dress, girl."
			},
			{
				"kz" : "ревидтер",
				"ru" : "ревмиды",
				"en" : "rheumides",
				"kz-def" : "Қараңғы диатез дамыған тері аурулары класы.",
				"ru-def" : "Класс кожных заболеваний, вызванных лёгким диатезом.",
				"en-def" : "The class of skin disease developed by the dartrous diathesis."
			},
			{
				"kz" : "жеңіл атлетизм",
				"ru" : "атлетизм",
				"en" : "athletism",
				"kz-def" : "Спортшының жағдайы немесе практикасы; спортшының сипаттамалары.",
				"ru-def" : "Состояние или практика спортсмена; характеристики спортсмена.",
				"en-def" : "The state or practice of an athlete; the characteristics of an athlete."
			},
			{
				"kz" : "пирономика",
				"ru" : "пирономика",
				"en" : "pyronomics",
				"kz-def" : "Жылу туралы ғылым.",
				"ru-def" : "Наука о тепле.",
				"en-def" : "The science of heat."
			},
			{
				"kz" : "пропаганда",
				"ru" : "пропаганда",
				"en" : "advocacy",
				"kz-def" : "Өтініш беру немесе қолдау көрсету әрекеті; ақпараттық-түсіндіру жұмысы; шапағат.",
				"ru-def" : "Акт мольбы или поддержки; адвокатская работа; заступничество.",
				"en-def" : "The act of pleading for or supporting; work of advocating; intercession."
			},
			{
				"kz" : "шағылысады",
				"ru" : "отражающий",
				"en" : "reflectible",
				"kz-def" : "Шағылыстыруға немесе кері лақтыруға қабілетті; рефлексиялық.",
				"ru-def" : "Способен отражаться или отбрасываться назад; непоколебимый.",
				"en-def" : "Capable of being reflected, or thrown back; reflexible."
			},
			{
				"kz" : "жетілдіріңіз",
				"ru" : "заражать",
				"en" : "enfect",
				"kz-def" : "Заңсыздықпен ластанған.",
				"ru-def" : "Загрязнен незаконностью.",
				"en-def" : "Contaminated with illegality."
			},
			{
				"kz" : "күн шуақтығы",
				"ru" : "солнечность",
				"en" : "sunniness",
				"kz-def" : "Күн шуақты болу сапасы немесе күйі.",
				"ru-def" : "Качество или состояние солнечного света.",
				"en-def" : "The quality or state of being sunny."
			}
			]
		}
	}
"""

data = json.loads(str_json)
print("Enter one word any of this languages: KZ, RU, ENG: ")
print()
word = input()
for item in data['response']['items']:
	if (word == item['kz'] or word == item['ru'] or word == item['en']):
		print(item['kz'] + " : " +  item['kz-def'])
		print("----------------------------------")
		print(item['ru'] + " : " +  item['ru-def'])
		print("----------------------------------")
		print(item['en'] + " : " +  item['en-def'])
		print("----------------------------------")
		break


