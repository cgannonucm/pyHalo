import numpy as np

def get_interps(vpower):

    if vpower == 0:
        zeta_values = np.array([15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
        delta_zeta = 10

        slopes_fit15 = np.array([-0.00873369, 0.04547522, -0.29734756])
        intercept_fit15 = np.array([0.07877708, -0.38898387, 10.5698512])

        slopes_fit20 = np.array([-0.00918773, 0.0488793, -0.29863145])
        intercept_fit20 = np.array([0.07010828, -0.36470976, 10.46369133])

        slopes_fit30 = np.array([-0.00241264, 0.02423532, -0.27256061])
        intercept_fit30 = np.array([4.88893147e-03, -1.17866173e-01, 1.01118786e+01])

        slopes_fit40 = np.array([-0.00290296, 0.02673381, -0.2688431])
        intercept_fit40 = np.array([6.07813845e-03, -1.21838139e-01, 1.00005009e+01])

        slopes_fit50 = np.array([0.00044168, 0.01763467, -0.26034332])
        intercept_fit50 = np.array([-0.02583692, -0.02511449, 9.86354876])

        slopes_fit60 = np.array([0.00093022, 0.01567164, -0.25349179])
        intercept_fit60 = np.array([-3.16140435e-02, 2.30547410e-03, 9.75835143e+00])

        slopes_fit70 = np.array([-0.00082639, 0.02240234, -0.25545913])
        intercept_fit70 = np.array([-0.01940403, -0.04151627, 9.73603133])

        slopes_fit80 = np.array([-2.40575064e-04, 2.22435083e-02, -2.53736741e-01])
        intercept_fit80 = np.array([-0.02435385, -0.03561933, 9.69079706])

        slopes_fit90 = np.array([-1.84122523e-04, 2.23516959e-02, -2.49861931e-01])
        intercept_fit90 = np.array([-0.02648198, -0.0264818, 9.62954199])

        slopes_fit100 = np.array([0.00107284, 0.01941302, -0.24634224])
        intercept_fit100 = np.array([-3.73727259e-02, 1.53168502e-03, 9.57909464e+00])

        slopes_fit110 = np.array([-4.55463887e-05, 2.31114321e-02, -2.46727988e-01])
        intercept_fit110 = np.array([-0.03068813, -0.01717815, 9.5574457])

        slopes_fit120 = np.array([-0.00051066, 0.0256819, -0.24616056])
        intercept_fit120 = np.array([-0.02726755, -0.03379491, 9.53504005])

        slope_polynomial = [slopes_fit15, slopes_fit20, slopes_fit30, slopes_fit40, slopes_fit50, slopes_fit60,
                            slopes_fit70, slopes_fit80, slopes_fit90, slopes_fit100, slopes_fit110, slopes_fit120]

        intercept_polynomial = [intercept_fit15, intercept_fit20, intercept_fit30, intercept_fit40, intercept_fit50,
                                intercept_fit60, intercept_fit70, intercept_fit80, intercept_fit90,
                                intercept_fit100, intercept_fit110, intercept_fit120]

    elif vpower == 0.25:

        zeta_values = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
        delta_zeta = 10

        v_power = 0.25

        slopes_fit5 = np.array([0.00265324, 0.0013187, -0.23389509])
        intercept_fit5 = np.array([-0.01416015, -0.0436715, 10.29509811])

        slopes_fit10 = np.array([-0.00244904, 0.01822089, -0.22663368])
        intercept_fit10 = np.array([0.01668281, -0.11724189, 9.95671085])

        slopes_fit20 = np.array([-0.00406356, 0.02438003, -0.22862712])
        intercept_fit20 = np.array([0.01234056, -0.0892347, 9.73510325])

        slopes_fit30 = np.array([0.00379082, -0.00085764, -0.20774859])
        intercept_fit30 = np.array([-0.05609376, 0.13923396, 9.45090133])

        slopes_fit40 = np.array([0.00022811, 0.01055014, -0.21209176])
        intercept_fit40 = np.array([-0.02789103, 0.05653192, 9.41670283])

        slopes_fit50 = np.array([0.00156431, 0.00819971, -0.20830772])
        intercept_fit50 = np.array([-0.04147038, 0.0899329, 9.32832227])

        slopes_fit60 = np.array([0.00185098, 0.008343, -0.20757718])
        intercept_fit60 = np.array([-0.04674078, 0.10276386, 9.2784344])

        slopes_fit70 = np.array([0.00265975, 0.00491357, -0.20274943])
        intercept_fit70 = np.array([-0.05378208, 0.13671694, 9.20575002])

        slopes_fit80 = np.array([0.00276225, 0.00710798, -0.20554342])
        intercept_fit80 = np.array([-0.05615454, 0.12678472, 9.20104849])

        slopes_fit90 = np.array([0.00167941, 0.01078237, -0.20590455])
        intercept_fit90 = np.array([-0.05054303, 0.11153491, 9.17377731])

        slopes_fit100 = np.array([0.00130484, 0.01211627, -0.20549199])
        intercept_fit100 = np.array([-0.04693703, 0.10302725, 9.15061961])

        slopes_fit110 = np.array([0.00151193, 0.01281393, -0.2050846])
        intercept_fit110 = np.array([-0.05048566, 0.10626126, 9.12707519])

        slopes_fit120 = np.array([0.00177043, 0.01211839, -0.20268432])
        intercept_fit120 = np.array([-0.05287078, 0.11606177, 9.09110859])

        slope_polynomial = [slopes_fit5, slopes_fit10, slopes_fit20, slopes_fit30, slopes_fit40, slopes_fit50,
                            slopes_fit60,
                            slopes_fit70, slopes_fit80, slopes_fit90, slopes_fit100, slopes_fit110, slopes_fit120]

        intercept_polynomial = [intercept_fit5, intercept_fit10, intercept_fit20, intercept_fit30, intercept_fit40,
                                intercept_fit50,
                                intercept_fit60, intercept_fit70, intercept_fit80, intercept_fit90,
                                intercept_fit100, intercept_fit110, intercept_fit120]

    elif vpower == 0.4:

        zeta_values = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
        delta_zeta = 10

        slopes_fit5 = np.array([0.15961935, -0.6056795, 0.27743768])
        intercept_fit5 = np.array([-1.19772122, 4.54910621, 6.3036186])

        slopes_fit10 = np.array([-0.00066629, 0.01213143, -0.19620701])
        intercept_fit10 = np.array([-1.12017166e-02, -7.26001369e-03, 9.59743358e+00])

        slopes_fit20 = np.array([0.00467656, -0.00875179, -0.17701287])
        intercept_fit20 = np.array([-0.0666846, 0.2160626, 9.23163342])

        slopes_fit30 = np.array([0.00280357, 0.00045004, -0.18216039])
        intercept_fit30 = np.array([-0.05221757, 0.15167468, 9.1749843])

        slopes_fit40 = np.array([0.00178267, 0.00395416, -0.18325958])
        intercept_fit40 = np.array([-0.04618201, 0.13696309, 9.11572964])

        slopes_fit50 = np.array([0.00209424, 0.00252393, -0.18106064])
        intercept_fit50 = np.array([-0.05096114, 0.16131746, 9.04605069])

        slopes_fit60 = np.array([0.00301758, 0.002483, -0.18321019])
        intercept_fit60 = np.array([-0.05972626, 0.16918253, 9.0259463])

        slopes_fit70 = np.array([0.00343449, 0.00115228, -0.18177905])
        intercept_fit70 = np.array([-0.06508904, 0.19271624, 8.97753326])

        slopes_fit80 = np.array([3.78459538e-03, -1.21050722e-04, -1.79476704e-01])
        intercept_fit80 = np.array([-0.06889257, 0.2106829, 8.93042337])

        slopes_fit90 = np.array([0.00279943, 0.00364632, -0.18093018])
        intercept_fit90 = np.array([-0.06191401, 0.1872276, 8.91996702])

        slopes_fit100 = np.array([0.00285508, 0.00400034, -0.18209596])
        intercept_fit100 = np.array([-0.06450729, 0.19490901, 8.90676437])

        slopes_fit110 = np.array([0.00415302, -0.00112172, -0.1762421])
        intercept_fit110 = np.array([-0.07595476, 0.24258089, 8.84230485])

        slopes_fit120 = np.array([0.00282095, 0.00537875, -0.18258776])
        intercept_fit120 = np.array([-0.06649255, 0.19674746, 8.87858429])

        slope_polynomial = [slopes_fit5, slopes_fit10, slopes_fit20, slopes_fit30, slopes_fit40, slopes_fit50,
                            slopes_fit60,
                            slopes_fit70, slopes_fit80, slopes_fit90, slopes_fit100, slopes_fit110, slopes_fit120]

        intercept_polynomial = [intercept_fit5, intercept_fit10, intercept_fit20, intercept_fit30, intercept_fit40,
                                intercept_fit50,
                                intercept_fit60, intercept_fit70, intercept_fit80, intercept_fit90,
                                intercept_fit100, intercept_fit110, intercept_fit120]

    elif vpower == 0.5:

        zeta_values = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
        delta_zeta = 10

        slopes_fit5 = np.array([0.0012989, -0.00151646, -0.15982686])
        intercept_fit5 = np.array([-0.01229278, 0.0428837, 9.49031537])

        slopes_fit10 = np.array([-0.00025443, 0.01007318, -0.17423818])
        intercept_fit10 = np.array([-0.0169306, 0.02538956, 9.363078])

        slopes_fit20 = np.array([0.00320873, -0.00437765, -0.16328214])
        intercept_fit20 = np.array([-0.05463304, 0.18431916, 9.08253523])

        slopes_fit30 = np.array([0.00308802, -0.00220246, -0.16433341])
        intercept_fit30 = np.array([-0.05864577, 0.19309639, 8.98506665])

        slopes_fit40 = np.array([0.00321089, -0.00261928, -0.16619568])
        intercept_fit40 = np.array([-0.06121329, 0.20783084, 8.93435083])

        slopes_fit50 = np.array([0.00248163, 0.00078203, -0.16693899])
        intercept_fit50 = np.array([-0.05739456, 0.19123372, 8.89263283])

        slopes_fit60 = np.array([0.00483479, -0.0057663, -0.16375015])
        intercept_fit60 = np.array([-0.07757196, 0.25334904, 8.82731654])

        slopes_fit70 = np.array([0.00465157, -0.00559884, -0.16428474])
        intercept_fit70 = np.array([-0.07582748, 0.2570401, 8.80085341])

        slopes_fit80 = np.array([0.00353611, -0.00084991, -0.16869627])
        intercept_fit80 = np.array([-0.06987584, 0.23252822, 8.80845793])

        slopes_fit90 = np.array([0.00476609, -0.00431403, -0.16640688])
        intercept_fit90 = np.array([-0.08219107, 0.27246728, 8.76596329])

        slopes_fit100 = np.array([0.0046619, -0.00344269, -0.1671239])
        intercept_fit100 = np.array([-0.08314166, 0.27455759, 8.75212681])

        slopes_fit110 = np.array([3.60339922e-03, 1.31360162e-04, -1.69504826e-01])
        intercept_fit110 = np.array([-0.07480173, 0.24838737, 8.7579539])

        slopes_fit120 = np.array([0.00449002, -0.00314914, -0.16767864])
        intercept_fit120 = np.array([-0.084442, 0.28699014, 8.72455021])

        slope_polynomial = [slopes_fit5, slopes_fit10, slopes_fit20, slopes_fit30, slopes_fit40, slopes_fit50,
                            slopes_fit60,
                            slopes_fit70, slopes_fit80, slopes_fit90, slopes_fit100, slopes_fit110, slopes_fit120]

        intercept_polynomial = [intercept_fit5, intercept_fit10, intercept_fit20, intercept_fit30, intercept_fit40,
                                intercept_fit50,
                                intercept_fit60, intercept_fit70, intercept_fit80, intercept_fit90,
                                intercept_fit100, intercept_fit110, intercept_fit120]

    elif vpower == 0.6:

        zeta_values = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
        delta_zeta = 10

        slopes_fit5 = np.array([0.00532636, -0.01548608, -0.13258164])
        intercept_fit5 = np.array([-0.0542423, 0.19769615, 9.1914769])

        slopes_fit10 = np.array([0.00293763, -0.00363292, -0.14594608])
        intercept_fit10 = np.array([-0.04713896, 0.15778479, 9.07856056])

        slopes_fit20 = np.array([0.00391073, -0.00694817, -0.14507455])
        intercept_fit20 = np.array([-0.06310773, 0.22103103, 8.88605547])

        slopes_fit30 = np.array([0.00354745, -0.00529315, -0.14761838])
        intercept_fit30 = np.array([-0.06342665, 0.2277179, 8.80870428])

        slopes_fit40 = np.array([0.0046871, -0.00689681, -0.15193929])
        intercept_fit40 = np.array([-0.07500406, 0.25314633, 8.78264004])

        slopes_fit50 = np.array([0.00588497, -0.01022511, -0.14838062])
        intercept_fit50 = np.array([-0.08722261, 0.29470006, 8.70281808])

        slopes_fit60 = np.array([0.0058367, -0.01147992, -0.14880548])
        intercept_fit60 = np.array([-0.08785315, 0.31421723, 8.66913953])

        slopes_fit70 = np.array([0.00479057, -0.00778304, -0.15202999])
        intercept_fit70 = np.array([-0.08236731, 0.29833731, 8.66421279])

        slopes_fit80 = np.array([0.0054714, -0.00831967, -0.15432778])
        intercept_fit80 = np.array([-0.08914859, 0.31142856, 8.65769244])

        slopes_fit90 = np.array([0.00557633, -0.00948703, -0.1530476])
        intercept_fit90 = np.array([-0.09116717, 0.32822673, 8.62772145])

        slopes_fit100 = np.array([0.00549166, -0.00790876, -0.15720378])
        intercept_fit100 = np.array([-0.09117963, 0.32292029, 8.64287672])

        slopes_fit110 = np.array([0.00560193, -0.00876665, -0.15554193])
        intercept_fit110 = np.array([-0.09636302, 0.34416616, 8.61085698])

        slopes_fit120 = np.array([0.00550915, -0.00813063, -0.15671411])
        intercept_fit120 = np.array([-0.0950345, 0.34060712, 8.61002036])

        slope_polynomial = [slopes_fit5, slopes_fit10, slopes_fit20, slopes_fit30, slopes_fit40, slopes_fit50,
                            slopes_fit60,
                            slopes_fit70, slopes_fit80, slopes_fit90, slopes_fit100, slopes_fit110, slopes_fit120]

        intercept_polynomial = [intercept_fit5, intercept_fit10, intercept_fit20, intercept_fit30, intercept_fit40,
                                intercept_fit50,
                                intercept_fit60, intercept_fit70, intercept_fit80, intercept_fit90,
                                intercept_fit100, intercept_fit110, intercept_fit120]

    elif vpower == 0.75:

        zeta_values = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
        delta_zeta = 10

        slopes_fit5 = np.array([0.0073363, -0.02420357, -0.09743076])
        intercept_fit5 = np.array([-0.08196289, 0.31987498, 8.7988166])

        slopes_fit10 = np.array([0.00495241, -0.01149054, -0.11406175])
        intercept_fit10 = np.array([-0.07120591, 0.25632146, 8.73628973])

        slopes_fit20 = np.array([0.00495698, -0.01178013, -0.11984633])
        intercept_fit20 = np.array([-0.07586772, 0.28437172, 8.61415064])

        slopes_fit30 = np.array([0.00499943, -0.01043922, -0.12621999])
        intercept_fit30 = np.array([-0.0795134, 0.29215373, 8.57422544])

        slopes_fit40 = np.array([0.00514806, -0.0125641, -0.12733293])
        intercept_fit40 = np.array([-0.08215261, 0.32048692, 8.52443904])

        slopes_fit50 = np.array([0.00576937, -0.01298645, -0.13094439])
        intercept_fit50 = np.array([-0.08940453, 0.33749282, 8.50861492])

        slopes_fit60 = np.array([0.00657674, -0.01635683, -0.13171033])
        intercept_fit60 = np.array([-0.09874747, 0.37915242, 8.47964869])

        slopes_fit70 = np.array([0.00721867, -0.01789994, -0.1337875])
        intercept_fit70 = np.array([-0.1066543, 0.40535467, 8.46740017])

        slopes_fit80 = np.array([0.00677051, -0.01602363, -0.13624527])
        intercept_fit80 = np.array([-0.10582565, 0.40272525, 8.46368238])

        slopes_fit90 = np.array([0.00676115, -0.01486285, -0.14071791])
        intercept_fit90 = np.array([-0.10639645, 0.39954191, 8.48195431])

        slopes_fit100 = np.array([0.00627056, -0.01415308, -0.14064908])
        intercept_fit100 = np.array([-0.10258477, 0.39774229, 8.46783375])

        slopes_fit110 = np.array([0.00612255, -0.01429915, -0.14259594])
        intercept_fit110 = np.array([-0.10294788, 0.40782717, 8.46947815])

        slopes_fit120 = np.array([0.00694064, -0.01748712, -0.14233947])
        intercept_fit120 = np.array([-0.11045529, 0.44054946, 8.45525846])

        slope_polynomial = [slopes_fit5, slopes_fit10, slopes_fit20, slopes_fit30, slopes_fit40, slopes_fit50,
                            slopes_fit60,
                            slopes_fit70, slopes_fit80, slopes_fit90, slopes_fit100, slopes_fit110, slopes_fit120]

        intercept_polynomial = [intercept_fit5, intercept_fit10, intercept_fit20, intercept_fit30, intercept_fit40,
                                intercept_fit50,
                                intercept_fit60, intercept_fit70, intercept_fit80, intercept_fit90,
                                intercept_fit100, intercept_fit110, intercept_fit120]

    elif vpower == 0.7:

        zeta_values = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
        delta_zeta = 10

        if True:
            slopes_fit5 = np.array([0.00973678, -0.03142519, -0.10343325])
            intercept_fit5 = np.array([-0.09799922, 0.36181552, 8.88336984])

            slopes_fit10 = np.array([0.00714848, -0.01957806, -0.11861516])
            intercept_fit10 = np.array([-0.08880488, 0.31876295, 8.79644261])

            slopes_fit20 = np.array([0.00411244, -0.00903825, -0.12928106])
            intercept_fit20 = np.array([-0.06723712, 0.25336723, 8.71316201])

            slopes_fit30 = np.array([0.00513231, -0.01154284, -0.13102058])
            intercept_fit30 = np.array([-0.07900466, 0.29230299, 8.6350889])

            slopes_fit40 = np.array([0.00411038, -0.00778135, -0.13599851])
            intercept_fit40 = np.array([-0.07365812, 0.27845067, 8.61030438])

            slopes_fit50 = np.array([0.00476455, -0.00881367, -0.13811168])
            intercept_fit50 = np.array([-0.07911127, 0.29318647, 8.58592318])

            slopes_fit60 = np.array([0.00656568, -0.01527028, -0.13717628])
            intercept_fit60 = np.array([-0.09664753, 0.36046842, 8.54096375])

            slopes_fit70 = np.array([0.00610427, -0.01403559, -0.13881117])
            intercept_fit70 = np.array([-0.09533585, 0.36328051, 8.525243])

            slopes_fit80 = np.array([0.00569853, -0.01228741, -0.14159118])
            intercept_fit80 = np.array([-0.09355446, 0.358146, 8.52499591])

            slopes_fit90 = np.array([0.00717163, -0.01529502, -0.14327842])
            intercept_fit90 = np.array([-0.10825774, 0.3949343, 8.51707394])

            slopes_fit100 = np.array([0.00580987, -0.01071642, -0.14694581])
            intercept_fit100 = np.array([-0.09798099, 0.36326058, 8.53191791])

            slopes_fit110 = np.array([0.00575655, -0.01198294, -0.14610312])
            intercept_fit110 = np.array([-0.09857626, 0.38093526, 8.50976205])

            slopes_fit120 = np.array([0.00601038, -0.01233357, -0.14800367])
            intercept_fit120 = np.array([-0.10127382, 0.38955701, 8.51349066])

        else:
            slopes_fit5 = np.array([-0.00196707, -0.11596073])
            intercept_fit5 = np.array([0.06532406, 9.00945706])

            slopes_fit10 = np.array([0.0020493, -0.12781251])
            intercept_fit10 = np.array([0.05008846, 8.91070026])

            slopes_fit20 = np.array([0.00340371, -0.13457218])
            intercept_fit20 = np.array([0.04994487, 8.79967026])

            slopes_fit30 = np.array([0.00398468, -0.13762388])
            intercept_fit30 = np.array([0.05327855, 8.73673745])

            slopes_fit40 = np.array([0.00465438, -0.14128698])
            intercept_fit40 = np.array([0.05560193, 8.70507398])

            slopes_fit50 = np.array([0.00560122, -0.14424182])
            intercept_fit50 = np.array([0.0538395, 8.68770889])

            slopes_fit60 = np.array([0.00459384, -0.14562378])
            intercept_fit60 = np.array([0.06806642, 8.66531186])

            slopes_fit70 = np.array([0.00443256, -0.14666501])
            intercept_fit70 = np.array([0.07484694, 8.64790349])

            slopes_fit80 = np.array([0.00495319, -0.14892299])
            intercept_fit80 = np.array([0.07510193, 8.64536443])

            slopes_fit90 = np.array([0.00640236, -0.15250554])
            intercept_fit90 = np.array([0.06740622, 8.65635991])

            slopes_fit100 = np.array([0.00686102, -0.15442087])
            intercept_fit100 = np.array([0.06682426, 8.65798167])

            slopes_fit110 = np.array([0.0054332, -0.15350959])
            intercept_fit110 = np.array([0.082698, 8.63659169])

            slopes_fit120 = np.array([0.00585052, -0.15573671])
            intercept_fit120 = np.array([0.08315841, 8.64379102])

        slope_polynomial = [slopes_fit5, slopes_fit10, slopes_fit20, slopes_fit30, slopes_fit40, slopes_fit50,
                            slopes_fit60,
                            slopes_fit70, slopes_fit80, slopes_fit90, slopes_fit100, slopes_fit110, slopes_fit120]

        intercept_polynomial = [intercept_fit5, intercept_fit10, intercept_fit20, intercept_fit30, intercept_fit40,
                                intercept_fit50,
                                intercept_fit60, intercept_fit70, intercept_fit80, intercept_fit90,
                                intercept_fit100, intercept_fit110, intercept_fit120]

    else:
        raise Exception('v_power '+str(vpower)+' not recognized.')

    return slope_polynomial, intercept_polynomial, zeta_values, delta_zeta

def _logrho_Mz(m, z, idx, slope_polynomial, intercept_polynomial):

    try:
        slope = slope_polynomial[idx][0] * z ** 2 + slope_polynomial[idx][1] * z + slope_polynomial[idx][2]
        intercept = intercept_polynomial[idx][0] * z ** 2 + intercept_polynomial[idx][1] * z + intercept_polynomial[idx][2]
    except:
        slope = slope_polynomial[idx][0] * z + slope_polynomial[idx][1]
        intercept = intercept_polynomial[idx][0] * z + intercept_polynomial[idx][1]
    # print(slope, intercept)

    return intercept + np.log10(m) * slope

def logrho_Mz_0(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_poly, intercept_poly):

    if zeta >= 15 and zeta < 20:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * 5 ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta > 20 and zeta <= 22.5:
        inds = [1, 2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta < zeta_values[0]:
        rho_0 = _logrho_Mz(m, z, 0, slope_poly, intercept_poly)
        logm = np.log10(m)

        if logm < 6:
            rho_at_0 = 10
        elif logm <= 7:
            rho_at_0 = 9
        elif logm <= 8:
            rho_at_0 = 8.8
        else:
            rho_at_0 = 8.5

        derivative = (rho_0 - rho_at_0) * delta_zeta ** -1

        logrho_central = (zeta - zeta_values[0]) * derivative + rho_0

    elif zeta > 120:
        nmax = int(len(zeta_values))-1
        rho_0 = _logrho_Mz(m, z, nmax, slope_poly, intercept_poly)
        derivative = (-_logrho_Mz(m, z, int(nmax-1)) + rho_0) * delta_zeta ** -1
        logrho_central = (zeta - zeta_values[-1]) * derivative + rho_0

    else:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        #w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    logrho_central += 0.5 * (c - cmean) * cmean ** -1

    return logrho_central

def logrho_Mz_25(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_poly, intercept_poly):

    if zeta >= 5 and zeta < 10:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * 5 ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta >= 10 and zeta < 12.5:
        inds = [1, 2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta < zeta_values[0]:
        rho_0 = _logrho_Mz(m, z, 0, slope_poly, intercept_poly)

        logm = np.log10(m)
        if logm < 6:
            rho_at_0 = 10
        elif logm <= 7:
            rho_at_0 = 9
        elif logm <= 8:
            rho_at_0 = 8.8
        else:
            rho_at_0 = 8.5

        derivative = (rho_0 - rho_at_0) * delta_zeta ** -1

        logrho_central = (zeta - zeta_values[0]) * derivative + rho_0

    elif zeta > 120:
        nmax = int(len(zeta_values))-1
        rho_0 = _logrho_Mz(m, z, nmax, slope_poly, intercept_poly)
        derivative = (-_logrho_Mz(m, z, int(nmax-1)) + rho_0, slope_poly, intercept_poly) * delta_zeta ** -1
        logrho_central = (zeta - zeta_values[-1]) * derivative + rho_0

    else:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        #w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    logrho_central += 0.5 * (c - cmean) * cmean ** -1

    return logrho_central


def logrho_Mz_4(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_poly, intercept_poly):

    if zeta >= 5 and zeta < 10:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * 5 ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta >= 10 and zeta < 12.5:
        inds = [1, 2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta < zeta_values[0]:
        rho_0 = _logrho_Mz(m, z, 0, slope_poly, intercept_poly)

        rho_at_0 = 10

        derivative = (rho_0 - rho_at_0) * delta_zeta ** -1

        logrho_central = (zeta - zeta_values[0]) * derivative + rho_0

    elif zeta > 120:
        nmax = int(len(zeta_values))-1
        rho_0 = _logrho_Mz(m, z, nmax, slope_poly, intercept_poly)
        derivative = (-_logrho_Mz(m, z, int(nmax-1)) + rho_0) * delta_zeta ** -1
        logrho_central = (zeta - zeta_values[-1]) * derivative + rho_0

    else:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        #w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    logrho_central += 0.5 * (c - cmean) * cmean ** -1

    return logrho_central

def logrho_Mz_5(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_poly, intercept_poly):

    if zeta >= 5 and zeta < 10:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * 5 ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta >= 10 and zeta < 12.5:
        inds = [1, 2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta < zeta_values[0]:
        rho_0 = _logrho_Mz(m, z, 0, slope_poly, intercept_poly)

        rho_at_0 = 10

        derivative = (rho_0 - rho_at_0) * delta_zeta ** -1

        logrho_central = (zeta - zeta_values[0]) * derivative + rho_0

    elif zeta > 120:
        nmax = int(len(zeta_values))-1
        rho_0 = _logrho_Mz(m, z, nmax, slope_poly, intercept_poly)
        derivative = (-_logrho_Mz(m, z, int(nmax-1), slope_poly, intercept_poly) + rho_0) * delta_zeta ** -1
        logrho_central = (zeta - zeta_values[-1]) * derivative + rho_0

    else:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        #w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    logrho_central += 0.5 * (c - cmean) * cmean ** -1

    return logrho_central

def logrho_Mz_6(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_poly, intercept_poly):

    if zeta >= 5 and zeta < 10:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * 5 ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta >= 10 and zeta < 12.5:
        inds = [1, 2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta < zeta_values[0]:
        rho_0 = _logrho_Mz(m, z, 0, slope_poly, intercept_poly)

        rho_at_0 = 10

        derivative = (rho_0 - rho_at_0) * delta_zeta ** -1

        logrho_central = (zeta - zeta_values[0]) * derivative + rho_0

    elif zeta > 120:
        nmax = int(len(zeta_values))-1
        rho_0 = _logrho_Mz(m, z, nmax, slope_poly, intercept_poly)
        derivative = (-_logrho_Mz(m, z, int(nmax-1), slope_poly, intercept_poly) + rho_0) * delta_zeta ** -1
        logrho_central = (zeta - zeta_values[-1]) * derivative + rho_0

    else:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        #w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    logrho_central += 0.5 * (c - cmean) * cmean ** -1

    return logrho_central

def logrho_Mz_7(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_poly, intercept_poly):

    if zeta >= 5 and zeta < 10:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * 5 ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta >= 10 and zeta < 12.5:
        inds = [1, 2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta < zeta_values[0]:
        rho_0 = _logrho_Mz(m, z, 0, slope_poly, intercept_poly)

        rho_at_0 = 10

        derivative = (rho_0 - rho_at_0) * delta_zeta ** -1

        logrho_central = (zeta - zeta_values[0]) * derivative + rho_0

    elif zeta > 120:
        nmax = int(len(zeta_values))-1
        rho_0 = _logrho_Mz(m, z, nmax, slope_poly, intercept_poly)
        derivative = (-_logrho_Mz(m, z, int(nmax-1), slope_poly, intercept_poly) + rho_0) * delta_zeta ** -1
        logrho_central = (zeta - zeta_values[-1]) * derivative + rho_0

    else:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        #w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    logrho_central += 0.5 * (c - cmean) * cmean ** -1

    return logrho_central

def logrho_Mz_75(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_poly, intercept_poly):

    if zeta >= 5 and zeta < 10:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * 5 ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta >= 10 and zeta < 12.5:
        inds = [1, 2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        # w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    elif zeta < zeta_values[0]:
        rho_0 = _logrho_Mz(m, z, 0, slope_poly, intercept_poly)

        rho_at_0 = 10

        derivative = (rho_0 - rho_at_0) * delta_zeta ** -1

        logrho_central = (zeta - zeta_values[0]) * derivative + rho_0

    elif zeta > 120:
        nmax = int(len(zeta_values))-1
        rho_0 = _logrho_Mz(m, z, nmax, slope_poly, intercept_poly)
        derivative = (-_logrho_Mz(m, z, int(nmax-1), slope_poly, intercept_poly) + rho_0) * delta_zeta ** -1
        logrho_central = (zeta - zeta_values[-1]) * derivative + rho_0

    else:

        inds = np.argsort(np.absolute(zeta_values - zeta))[0:2]

        w1 = np.absolute(1 - np.absolute(zeta - zeta_values[inds[0]]) * delta_zeta ** -1)
        w2 = 1 - w1
        #w1, w2 = 1, 0

        rho1 = w1 * _logrho_Mz(m, z, inds[0], slope_poly, intercept_poly)
        rho2 = w2 * _logrho_Mz(m, z, inds[1], slope_poly, intercept_poly)

        logrho_central = rho1 + rho2

    logrho_central += 0.5 * (c - cmean) * cmean ** -1

    return logrho_central

def logrho(m, z, zeta, cmean, c, vpower):

    slope_polynomial, intercept_polynomial, zeta_values, delta_zeta = get_interps(vpower)

    if vpower == 0:
        return logrho_Mz_0(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_polynomial, intercept_polynomial)
    elif vpower == 0.25:
        return logrho_Mz_25(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_polynomial, intercept_polynomial)
    elif vpower == 0.4:
        return logrho_Mz_4(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_polynomial, intercept_polynomial)
    elif vpower == 0.5:
        return logrho_Mz_5(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_polynomial, intercept_polynomial)
    elif vpower == 0.6:
        return logrho_Mz_6(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_polynomial, intercept_polynomial)
    elif vpower == 0.7:
        return logrho_Mz_7(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_polynomial, intercept_polynomial)
    elif vpower == 0.75:
        return logrho_Mz_75(m, z, zeta, cmean, c, zeta_values, delta_zeta, slope_polynomial, intercept_polynomial)