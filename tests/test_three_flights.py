import copy
from unittest import TestCase

import numpy as np

from two_d_nav.envs.three_flights import ThreeFlights


class TestThreeFlights(TestCase):
    def setUp(self) -> None:
        self.env = ThreeFlights()
        plan_1 = np.array([[201.0, 698.2814322612103], [202.0, 696.536785101113], [203.0, 694.7658172581243],
                           [204.0, 692.9682908229911],
                           [205.0, 691.143971479737], [206.0, 689.2926287517669], [207.0, 687.4140362530215],
                           [208.0, 685.5079719440693],
                           [209.0, 683.5742183929991], [210.0, 681.6125630409744], [211.0, 679.6227984722834],
                           [212.0, 677.6047226887143],
                           [213.0, 675.5581393880619], [214.0, 673.4828582465616], [215.0, 671.3786952050272],
                           [216.0, 669.2454727584541],
                           [217.0, 667.0830202488324], [218.0, 664.8911741608977], [219.0, 662.6697784205289],
                           [220.0, 660.4186846954897],
                           [221.0, 658.1377526981853], [222.0, 655.8268504900959], [223.0, 653.4858547875278],
                           [224.0, 651.1146512683042],
                           [225.0, 648.7131348790035], [226.0, 646.2812101423337], [227.0, 643.8187914642153],
                           [228.0, 641.325803440127],
                           [229.0, 638.8021811602547], [230.0, 636.2478705129657], [231.0, 633.6628284861158],
                           [232.0, 631.0470234656807],
                           [233.0, 628.4004355311915], [234.0, 625.7230567474362], [235.0, 623.0148914518793],
                           [236.0, 620.275956537239],
                           [237.0, 617.506281728648], [238.0, 614.7059098548162], [239.0, 611.8748971126033],
                           [240.0, 609.013313324401],
                           [241.0, 606.1212421877176], [242.0, 603.1987815163532], [243.0, 600.2460434725479],
                           [244.0, 597.2631547894835],
                           [245.0, 594.2502569835191], [246.0, 591.207506555538], [247.0, 588.1350751807886],
                           [248.0, 585.0331498866044],
                           [249.0, 581.9019332173932], [250.0, 578.7416433862929], [251.0, 575.5525144129012],
                           [252.0, 572.3347962464965],
                           [253.0, 569.0887548741812], [254.0, 565.8146724133926], [255.0, 562.5128471882435],
                           [256.0, 559.1835937891747],
                           [257.0, 555.8272431154205], [258.0, 552.4441423998139], [259.0, 549.0346552154795],
                           [260.0, 545.5991614639926],
                           [261.0, 542.1380573446099], [262.0, 538.6517553042079], [263.0, 535.1406839675979],
                           [264.0, 531.6052880479224],
                           [265.0, 528.0460282368716], [266.0, 524.4633810744979], [267.0, 520.8578387984448],
                           [268.0, 517.2299091724511],
                           [269.0, 513.5801152940259], [270.0, 509.90899538124313], [271.0, 506.21710253864256],
                           [272.0, 502.5050045022708], [273.0, 498.77328336394595], [274.0, 495.0225352748731],
                           [275.0, 491.2533701287887], [276.0, 487.4664112248579], [277.0, 483.662294910601],
                           [278.0, 479.84167020517054],
                           [279.0, 476.0051984033511], [280.0, 472.15355266070367], [281.0, 468.28741756032156],
                           [282.0, 464.4074886617154], [283.0, 460.51447203238905], [284.0, 456.6090837627167],
                           [285.0, 452.6920494647727], [286.0, 448.7641037558128], [287.0, 444.82598972714385],
                           [288.0, 440.8784583991613], [289.0, 436.9222681633718], [290.0, 432.9581842122535],
                           [291.0, 428.98697795784204], [292.0, 425.0094264399611], [293.0, 421.02631172504687],
                           [294.0, 417.03842029654146], [295.0, 413.0465424378549], [296.0, 409.05147160891755],
                           [297.0, 405.05400381736183], [298.0, 401.05493698538925], [299.0, 397.0550703133895],
                           [300.0, 393.0552036413897], [301.0, 389.0561368094171], [302.0, 385.0586690178614],
                           [303.0, 381.06359818892406], [304.0, 377.07172033023744], [305.0, 373.0838289017321],
                           [306.0, 369.10071418681787], [307.0, 365.12316266893697], [308.0, 361.15195641452544],
                           [309.0, 357.1878724634072], [310.0, 353.2316822276176], [311.0, 349.28415089963516],
                           [312.0, 345.34603687096615], [313.0, 341.41809116200625], [314.0, 337.5010568640623],
                           [315.0, 333.59566859438996], [316.0, 329.7026519650635], [317.0, 325.82272306645746],
                           [318.0, 321.9565879660753], [319.0, 318.1049422234279], [320.0, 314.2684704216084],
                           [321.0, 310.447845716178],
                           [322.0, 306.64372940192106], [323.0, 302.8567704979903], [324.0, 299.08760535190584],
                           [325.0, 295.33685726283306], [326.0, 291.60513612450814], [327.0, 287.89303808813634],
                           [328.0, 284.2011452455358], [329.0, 280.5300253327531], [330.0, 276.8802314543278],
                           [331.0, 273.2523018283341],
                           [332.0, 269.6467595522811], [333.0, 266.06411238990734], [334.0, 262.50485257885657],
                           [335.0, 258.9694566591811], [336.0, 255.45838532257108], [337.0, 251.97208328216902],
                           [338.0, 248.51097916278638], [339.0, 245.0754854112995], [340.0, 241.66599822696503],
                           [341.0, 238.28289751135844], [342.0, 234.9265468376043], [343.0, 231.59729343853542],
                           [344.0, 228.29546821338636], [345.0, 225.02138575259767], [346.0, 221.77534438028238],
                           [347.0, 218.5576262138776], [348.0, 215.3684972404859], [349.0, 212.20820740938552],
                           [350.0, 209.07699074017444], [351.0, 205.97506544599025], [352.0, 202.90263407124087],
                           [353.0, 199.85988364325976], [354.0, 196.8469858372954], [355.0, 193.864097154231],
                           [356.0, 190.91135911042556], [357.0, 187.98889843906113], [358.0, 185.09682730237773],
                           [359.0, 182.2352435141754], [360.0, 179.4042307719625], [361.0, 176.60385889813074],
                           [362.0, 173.8341840895398], [363.0, 171.09524917489944], [364.0, 168.38708387934253],
                           [365.0, 165.7097050955872], [366.0, 163.06311716109803], [367.0, 160.44731214066292],
                           [368.0, 157.862270113813], [369.0, 155.30795946652404], [370.0, 152.78433718665178],
                           [371.0, 150.2913491625635], [372.0, 147.82893048444498], [373.0, 145.39700574777532],
                           [374.0, 142.99548935847452], [375.0, 140.6242858392509], [376.0, 138.2832901366828],
                           [377.0, 135.97238792859343], [378.0, 133.69145593128906], [379.0, 131.4403622062498],
                           [380.0, 129.21896646588107], [381.0, 127.0271203779464], [382.0, 124.86466786832466],
                           [383.0, 122.73144542175169], [384.0, 120.62728238021725], [385.0, 118.55200123871691],
                           [386.0, 116.50541793806451], [387.0, 114.48734215449542], [388.0, 112.49757758580449],
                           [389.0, 110.53592223377973], [390.0, 108.60216868270959], [391.0, 106.69610437375718],
                           [392.0, 104.81751187501197], [393.0, 102.9661691470418], [394.0, 101.14184980378786],
                           [395.0, 99.34432336865461], [396.0, 97.57335552566599], [397.0, 95.82870836556867],
                           [398.0, 94.11014062677896],
                           [399.0, 92.41740793108352], [400.0, 90.75026301401385], [401.0, 89.10845594982925],
                           [402.0, 87.49173437105264],
                           [403.0, 85.89984368251544], [404.0, 84.33252726987985], [405.0, 82.78952670261197],
                           [406.0, 81.27058193139726],
                           [407.0, 79.77543147998904], [408.0, 78.30381263149889], [409.0, 76.85546160913759],
                           [410.0, 75.4301137514326],
                           [411.0, 74.0275036819437], [412.0, 72.64736547351697], [413.0, 71.28943280711508],
                           [414.0, 69.95343912527437],
                           [415.0, 68.63911778023862], [416.0, 67.3462021768305], [417.0, 66.07442591012284],
                           [418.0, 64.82352289797814],
                           [419.0, 63.593227508527434], [420.0, 62.38327468266516], [421.0, 61.1934000516394],
                           [422.0, 60.02334004981765],
                           [423.0, 58.872832022717375], [424.0, 57.74161433038432], [425.0, 56.62942644621194],
                           [426.0, 55.53600905129201], [427.0, 54.461104124390545], [428.0, 53.40445502764305],
                           [429.0, 52.36580658806702], [430.0, 51.344905174985115], [431.0, 50.341498773462035],
                           [432.0, 49.35533705384751], [433.0, 48.386171437528674], [434.0, 47.43375515898674],
                           [435.0, 46.497843324260316], [436.0, 45.57819296591117], [437.0, 44.67456309459067],
                           [438.0, 43.78671474730652], [439.0, 42.914411032484395], [440.0, 42.05741717192336],
                           [441.0, 41.21550053973692], [442.0, 40.38843069837833], [443.0, 39.57597943184055],
                           [444.0, 38.777920776123665], [445.0, 37.99403104706289], [446.0, 37.22408886560265],
                           [447.0, 36.467875180610804], [448.0, 35.725173289313716], [449.0, 34.995768855442975],
                           [450.0, 34.27944992517473], [451.0, 33.57600694094447], [452.0, 32.885232753218816],
                           [453.0, 32.20692263030253], [454.0, 31.54087426625847], [455.0, 30.886887787016576],
                           [456.0, 30.24476575474614], [457.0, 29.614313170562582], [458.0, 28.995337475640554],
                           [459.0, 28.387648550800918], [460.0, 27.79105871464185], [461.0, 27.2053827202742],
                           [462.0, 26.630437750731062], [463.0, 26.06604341310822], [464.0, 25.512021731498407],
                           [465.0, 24.96819713877892], [466.0, 24.434396467306215], [467.0, 23.910448938575428],
                           [468.0, 23.39618615189852], [469.0, 22.891442072149857], [470.0, 22.396053016634596],
                           [471.0, 21.90985764112338], [472.0, 21.43269692510478], [473.0, 20.964414156298517],
                           [474.0, 20.50485491447455], [475.0, 20.05386705462149], [476.0, 19.611300689503537],
                           [477.0, 19.177008171647913], [478.0, 18.750844074799943], [479.0, 18.332665174882095],
                           [480.0, 17.922330430495776], [481.0, 17.519700962995557], [482.0, 17.124640036173332],
                           [483.0, 16.73701303558107], [484.0, 16.35668744752479], [485.0, 15.983532837758503],
                           [486.0, 15.617420829904745], [487.0, 15.258225083632624], [488.0, 14.905821272615299],
                           [489.0, 14.56008706229386], [490.0, 14.220902087472268], [491.0, 13.888147929764045],
                           [492.0, 13.561708094914366], [493.0, 13.241467990017782], [494.0, 12.927314900651481],
                           [495.0, 12.61913796794397], [496.0, 12.316828165596007], [497.0, 12.020278276873114],
                           [498.0, 11.729382871584107], [499.0, 11.444038283062696], [500.0, 11.16414258516761]])
        plan_1[:, 0] += 40
        plan_2 = copy.deepcopy(plan_1)
        plan_2[:, 0] += 100
        plan_3 = copy.deepcopy(plan_1)
        plan_3[:, 0] += 200

        plan_1 = np.stack([plan_1[:-1], plan_1[1:]], axis=1)
        plan_2 = np.stack([plan_2[:-1], plan_2[1:]], axis=1)
        plan_3 = np.stack([plan_3[:-1], plan_3[1:]], axis=1)

        self.env.engine.set_plan_groups([[plan_1, plan_2, plan_3]])

    def test_render(self):
        for _ in range(300):
            self.env.step([])
            self.env.render()

        print(self.env.res)

        self.env.reset()
        for _ in range(300):
            self.env.step("safe")
            self.env.render()
