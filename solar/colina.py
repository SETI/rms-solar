################################################################################
# solar/colina.py: Colina model for the solar flux density at 1 AU.
#
# From Colina, L., R. C. Bohlin, and F. Castelli, 1996. The 0.12-2.5 micron
# absolute flux distribution of the Sun for comparison with solar analog stars.
# Astron. J. 112, 307-315.
################################################################################

import numpy as np
import tabulation as tab

# Column 1 is wavelength in microns
# Column 2 is solar F (not flux density) at 1 AU in W/m^2/Hz

COLINA_ARRAY = np.array([
    0.119500, 1.34269e-18,
    0.120500, 1.06999e-17,
    0.121500, 9.52491e-17,
    0.122500, 2.28803e-17,
    0.123500, 1.01461e-18,
    0.124500, 6.70275e-19,
    0.125500, 5.64521e-19,
    0.126500, 7.06755e-19,
    0.127500, 4.16554e-19,
    0.128500, 3.42433e-19,
    0.129500, 8.30623e-19,
    0.130500, 2.49545e-18,
    0.131500, 8.22167e-19,
    0.132500, 8.66106e-19,
    0.133500, 3.65061e-18,
    0.134500, 9.71820e-19,
    0.135500, 8.17521e-19,
    0.136500, 6.78593e-19,
    0.137500, 6.47147e-19,
    0.138500, 9.14775e-19,
    0.139500, 1.83748e-18,
    0.140500, 1.42836e-18,
    0.141500, 9.79902e-19,
    0.142500, 1.10336e-18,
    0.143500, 1.21897e-18,
    0.144500, 1.23414e-18,
    0.145500, 1.35663e-18,
    0.146500, 1.75199e-18,
    0.147500, 2.12249e-18,
    0.148500, 2.07099e-18,
    0.149500, 2.04349e-18,
    0.150500, 2.25837e-18,
    0.151500, 2.43692e-18,
    0.152500, 3.13014e-18,
    0.153500, 3.53133e-18,
    0.154500, 5.73032e-18,
    0.155500, 6.01256e-18,
    0.156500, 5.15069e-18,
    0.157500, 4.85219e-18,
    0.158500, 4.78339e-18,
    0.159500, 5.05043e-18,
    0.160500, 5.65788e-18,
    0.161500, 6.59066e-18,
    0.162500, 7.57332e-18,
    0.163500, 8.75741e-18,
    0.164500, 9.22951e-18,
    0.165500, 1.34151e-17,
    0.166500, 1.25718e-17,
    0.167500, 1.23288e-17,
    0.168500, 1.45822e-17,
    0.169500, 1.90190e-17,
    0.170500, 2.16453e-17,
    0.171500, 2.28768e-17,
    0.172500, 2.43741e-17,
    0.173500, 2.59527e-17,
    0.174500, 3.11314e-17,
    0.175500, 3.74844e-17,
    0.176500, 4.29370e-17,
    0.177500, 5.00440e-17,
    0.178500, 5.56467e-17,
    0.179500, 5.76053e-17,
    0.180500, 6.77727e-17,
    0.181500, 8.38527e-17,
    0.182500, 8.46909e-17,
    0.183500, 8.54608e-17,
    0.184500, 7.92253e-17,
    0.185500, 8.95792e-17,
    0.186500, 1.05919e-16,
    0.187500, 1.19293e-16,
    0.188500, 1.31747e-16,
    0.189500, 1.44541e-16,
    0.190500, 1.53733e-16,
    0.191500, 1.72064e-16,
    0.192500, 1.72116e-16,
    0.193500, 1.60183e-16,
    0.194500, 2.22012e-16,
    0.195500, 2.33932e-16,
    0.196500, 2.60995e-16,
    0.197500, 2.71977e-16,
    0.198500, 2.74069e-16,
    0.199500, 2.97805e-16,
    0.200500, 3.30848e-16,
    0.201500, 3.66079e-16,
    0.202500, 3.79881e-16,
    0.203500, 4.28110e-16,
    0.204500, 4.80783e-16,
    0.205500, 5.00059e-16,
    0.206500, 5.30275e-16,
    0.207500, 6.12630e-16,
    0.208500, 7.31097e-16,
    0.209500, 1.03990e-15,
    0.210500, 1.37120e-15,
    0.211500, 1.66168e-15,
    0.212500, 1.56699e-15,
    0.213500, 1.66689e-15,
    0.214500, 2.03697e-15,
    0.215500, 1.85841e-15,
    0.216500, 1.67279e-15,
    0.217500, 1.84036e-15,
    0.218500, 2.34110e-15,
    0.219500, 2.49932e-15,
    0.220500, 2.54485e-15,
    0.221500, 2.14450e-15,
    0.222500, 2.70889e-15,
    0.223500, 3.46657e-15,
    0.224500, 3.27573e-15,
    0.225500, 2.93781e-15,
    0.226500, 2.23724e-15,
    0.227500, 2.27021e-15,
    0.228500, 2.98963e-15,
    0.229500, 2.76912e-15,
    0.230500, 3.05319e-15,
    0.231500, 3.01122e-15,
    0.232500, 3.17036e-15,
    0.233500, 2.69786e-15,
    0.234500, 2.36627e-15,
    0.235500, 3.13942e-15,
    0.236500, 2.99997e-15,
    0.237500, 3.01701e-15,
    0.238500, 2.63206e-15,
    0.239500, 2.79599e-15,
    0.240500, 2.52204e-15,
    0.241500, 3.29617e-15,
    0.242500, 4.57020e-15,
    0.243500, 4.34437e-15,
    0.244500, 4.02143e-15,
    0.245500, 3.29116e-15,
    0.246500, 3.38153e-15,
    0.247500, 3.75057e-15,
    0.248500, 3.11131e-15,
    0.249500, 3.86988e-15,
    0.250500, 4.17228e-15,
    0.251500, 3.22581e-15,
    0.252500, 2.92139e-15,
    0.253500, 3.65574e-15,
    0.254500, 4.25814e-15,
    0.255500, 5.69637e-15,
    0.256500, 7.36479e-15,
    0.257500, 9.15304e-15,
    0.258500, 9.20300e-15,
    0.259500, 7.75243e-15,
    0.260500, 6.41940e-15,
    0.261500, 6.75103e-15,
    0.262500, 7.89616e-15,
    0.263500, 1.24909e-14,
    0.264500, 1.92332e-14,
    0.265500, 1.96370e-14,
    0.266500, 1.95139e-14,
    0.267500, 1.97859e-14,
    0.268500, 1.93795e-14,
    0.269500, 1.91195e-14,
    0.270500, 2.15520e-14,
    0.271500, 1.82195e-14,
    0.272500, 1.61400e-14,
    0.273500, 1.62983e-14,
    0.274500, 1.10451e-14,
    0.275500, 1.46209e-14,
    0.276500, 2.04461e-14,
    0.277500, 1.98793e-14,
    0.278500, 1.36119e-14,
    0.279500, 7.50850e-15,
    0.280500, 8.33037e-15,
    0.281500, 1.82368e-14,
    0.282500, 2.58056e-14,
    0.283500, 2.77411e-14,
    0.284500, 2.10194e-14,
    0.285500, 1.46680e-14,
    0.286500, 2.90368e-14,
    0.287500, 3.05115e-14,
    0.288500, 2.93994e-14,
    0.289500, 4.35028e-14,
    0.290500, 5.57442e-14,
    0.291500, 5.42579e-14,
    0.292500, 4.89752e-14,
    0.293500, 5.06817e-14,
    0.294500, 4.84786e-14,
    0.295500, 5.29174e-14,
    0.296500, 4.90460e-14,
    0.297500, 4.92694e-14,
    0.298500, 4.55690e-14,
    0.299500, 4.77355e-14,
    0.300500, 4.17886e-14,
    0.301500, 4.55973e-14,
    0.302500, 4.92160e-14,
    0.303500, 6.29952e-14,
    0.304500, 6.15369e-14,
    0.305500, 6.10752e-14,
    0.306500, 5.75185e-14,
    0.307500, 6.40597e-14,
    0.308500, 6.41336e-14,
    0.309500, 5.24908e-14,
    0.310500, 6.63080e-14,
    0.311500, 7.78755e-14,
    0.312500, 7.05428e-14,
    0.313500, 7.56877e-14,
    0.314500, 7.22200e-14,
    0.315500, 6.93743e-14,
    0.316500, 6.97244e-14,
    0.317500, 8.58353e-14,
    0.318500, 7.43056e-14,
    0.319500, 7.99990e-14,
    0.320500, 9.09963e-14,
    0.321500, 7.96163e-14,
    0.322500, 7.88488e-14,
    0.323500, 7.62016e-14,
    0.324500, 8.82206e-14,
    0.325500, 1.02289e-13,
    0.326500, 1.14863e-13,
    0.327500, 1.12472e-13,
    0.328500, 1.09015e-13,
    0.329500, 1.26718e-13,
    0.330500, 1.22099e-13,
    0.331500, 1.16758e-13,
    0.332500, 1.16214e-13,
    0.333500, 1.12689e-13,
    0.334500, 1.17996e-13,
    0.335500, 1.16750e-13,
    0.336500, 1.00873e-13,
    0.337500, 1.05583e-13,
    0.338500, 1.16227e-13,
    0.339500, 1.21617e-13,
    0.340500, 1.28307e-13,
    0.341500, 1.18606e-13,
    0.342500, 1.28263e-13,
    0.343500, 1.23574e-13,
    0.344500, 1.04127e-13,
    0.345500, 1.23301e-13,
    0.346500, 1.22391e-13,
    0.347500, 1.19825e-13,
    0.348500, 1.20039e-13,
    0.349500, 1.19796e-13,
    0.350500, 1.41755e-13,
    0.351500, 1.33257e-13,
    0.352500, 1.24247e-13,
    0.353500, 1.42071e-13,
    0.354500, 1.53410e-13,
    0.355500, 1.45359e-13,
    0.356500, 1.27124e-13,
    0.357500, 1.12005e-13,
    0.358500, 9.83348e-14,
    0.359500, 1.41312e-13,
    0.360500, 1.38583e-13,
    0.361500, 1.26451e-13,
    0.362500, 1.44377e-13,
    0.363500, 1.44965e-13,
    0.364500, 1.48160e-13,
    0.365500, 1.69598e-13,
    0.366500, 1.82285e-13,
    0.367500, 1.75615e-13,
    0.368500, 1.64757e-13,
    0.369500, 1.84702e-13,
    0.370500, 1.72668e-13,
    0.371500, 1.78653e-13,
    0.372500, 1.61434e-13,
    0.373500, 1.41720e-13,
    0.374500, 1.39414e-13,
    0.375500, 1.65017e-13,
    0.376500, 1.69657e-13,
    0.377500, 2.01179e-13,
    0.378500, 2.09086e-13,
    0.379500, 1.69239e-13,
    0.380500, 1.91331e-13,
    0.381500, 1.72726e-13,
    0.382500, 1.27217e-13,
    0.383500, 1.10944e-13,
    0.384500, 1.55798e-13,
    0.385500, 1.64857e-13,
    0.386500, 1.65317e-13,
    0.387500, 1.65536e-13,
    0.388500, 1.63269e-13,
    0.389500, 1.95500e-13,
    0.390500, 2.08640e-13,
    0.391500, 2.25647e-13,
    0.392500, 1.72778e-13,
    0.393500, 9.93242e-14,
    0.394500, 1.75534e-13,
    0.395500, 2.25800e-13,
    0.396500, 1.47468e-13,
    0.397500, 1.60744e-13,
    0.398500, 2.65634e-13,
    0.399500, 2.91693e-13,
    0.400500, 2.96474e-13,
    0.401500, 3.09929e-13,
    0.402500, 3.13796e-13,
    0.403500, 3.02228e-13,
    0.404500, 3.01731e-13,
    0.405500, 3.02091e-13,
    0.406500, 2.89469e-13,
    0.407500, 2.97414e-13,
    0.408500, 3.18617e-13,
    0.409500, 3.15998e-13,
    0.410500, 2.68910e-13,
    0.411500, 3.27357e-13,
    0.412500, 3.23895e-13,
    0.413500, 3.19299e-13,
    0.414500, 3.17381e-13,
    0.415500, 3.18365e-13,
    0.416500, 3.39962e-13,
    0.417500, 3.08676e-13,
    0.418500, 3.13687e-13,
    0.419500, 3.18362e-13,
    0.420500, 3.30576e-13,
    0.421500, 3.39690e-13,
    0.422500, 3.00393e-13,
    0.423500, 3.26366e-13,
    0.424500, 3.38807e-13,
    0.425500, 3.26382e-13,
    0.426500, 3.28497e-13,
    0.427500, 3.05024e-13,
    0.428500, 3.09960e-13,
    0.429500, 2.89486e-13,
    0.430500, 2.23780e-13,
    0.431500, 3.33873e-13,
    0.432500, 3.27484e-13,
    0.433500, 3.45948e-13,
    0.434500, 3.35327e-13,
    0.435500, 3.47538e-13,
    0.436500, 3.90983e-13,
    0.437500, 3.67797e-13,
    0.438500, 3.20515e-13,
    0.439500, 3.75061e-13,
    0.440500, 3.53505e-13,
    0.441500, 4.00406e-13,
    0.442500, 4.12402e-13,
    0.443500, 3.99450e-13,
    0.444500, 4.14671e-13,
    0.445500, 3.84529e-13,
    0.446500, 4.01065e-13,
    0.447500, 4.42385e-13,
    0.448500, 4.22167e-13,
    0.449500, 4.35629e-13,
    0.450500, 4.62764e-13,
    0.451500, 4.57250e-13,
    0.452500, 4.22779e-13,
    0.453500, 4.30978e-13,
    0.454500, 4.34853e-13,
    0.455500, 4.48877e-13,
    0.456500, 4.60358e-13,
    0.457500, 4.67485e-13,
    0.458500, 4.40757e-13,
    0.459500, 4.51195e-13,
    0.460500, 4.60136e-13,
    0.461500, 4.65526e-13,
    0.462500, 4.78667e-13,
    0.463500, 4.66151e-13,
    0.464500, 4.53513e-13,
    0.465500, 4.70642e-13,
    0.466500, 4.44727e-13,
    0.467500, 4.68434e-13,
    0.468500, 4.65549e-13,
    0.469500, 4.66603e-13,
    0.470500, 4.42051e-13,
    0.471500, 4.77191e-13,
    0.472500, 4.84666e-13,
    0.473500, 4.74825e-13,
    0.474500, 4.91167e-13,
    0.475500, 4.84843e-13,
    0.476500, 4.72429e-13,
    0.477500, 5.03203e-13,
    0.478500, 4.89279e-13,
    0.479500, 5.07671e-13,
    0.480500, 4.99747e-13,
    0.481500, 5.15359e-13,
    0.482500, 5.00952e-13,
    0.483500, 5.02038e-13,
    0.484500, 4.91664e-13,
    0.485500, 4.58932e-13,
    0.486500, 4.09091e-13,
    0.487500, 4.62720e-13,
    0.488500, 4.85889e-13,
    0.489500, 4.99576e-13,
    0.490500, 5.13617e-13,
    0.491500, 4.87262e-13,
    0.492500, 4.89247e-13,
    0.493500, 4.89168e-13,
    0.494500, 5.35261e-13,
    0.495500, 5.03041e-13,
    0.496500, 5.28875e-13,
    0.497500, 5.31270e-13,
    0.498500, 4.93330e-13,
    0.499500, 5.22843e-13,
    0.500500, 4.94904e-13,
    0.501500, 4.84875e-13,
    0.502500, 5.08781e-13,
    0.503500, 5.21567e-13,
    0.504500, 5.06087e-13,
    0.505500, 5.41715e-13,
    0.506500, 5.35150e-13,
    0.507500, 5.22235e-13,
    0.508500, 5.27862e-13,
    0.509500, 5.29114e-13,
    0.510500, 5.39765e-13,
    0.511500, 5.55762e-13,
    0.512500, 5.21707e-13,
    0.513500, 5.22067e-13,
    0.514500, 5.27753e-13,
    0.515500, 5.37138e-13,
    0.516500, 4.73555e-13,
    0.517500, 4.91587e-13,
    0.518500, 4.72950e-13,
    0.519500, 5.24888e-13,
    0.520500, 5.27773e-13,
    0.521500, 5.51446e-13,
    0.522500, 5.29520e-13,
    0.523500, 5.52194e-13,
    0.524500, 5.72987e-13,
    0.525500, 5.66970e-13,
    0.526500, 4.93540e-13,
    0.527500, 5.41179e-13,
    0.528500, 5.63682e-13,
    0.529500, 5.72064e-13,
    0.530500, 5.84380e-13,
    0.531500, 5.89882e-13,
    0.532500, 5.34037e-13,
    0.533500, 5.82250e-13,
    0.534500, 5.64731e-13,
    0.535500, 6.07009e-13,
    0.536500, 5.72935e-13,
    0.537500, 5.78445e-13,
    0.538500, 5.87369e-13,
    0.539500, 5.67317e-13,
    0.540500, 5.49893e-13,
    0.541500, 5.86775e-13,
    0.542500, 5.71458e-13,
    0.543500, 5.90491e-13,
    0.544500, 5.92666e-13,
    0.545500, 6.01791e-13,
    0.546500, 5.97028e-13,
    0.547500, 5.84584e-13,
    0.548500, 5.96298e-13,
    0.549500, 6.08727e-13,
    0.550500, 6.00333e-13,
    0.551500, 6.05421e-13,
    0.552500, 5.99521e-13,
    0.553500, 6.13395e-13,
    0.554500, 6.20834e-13,
    0.555500, 6.22748e-13,
    0.556500, 6.00018e-13,
    0.557500, 6.10421e-13,
    0.558500, 5.93086e-13,
    0.559500, 6.02187e-13,
    0.560500, 6.16008e-13,
    0.561500, 6.11852e-13,
    0.562500, 6.22762e-13,
    0.563500, 6.28685e-13,
    0.564500, 6.28551e-13,
    0.565500, 6.11779e-13,
    0.566500, 6.24500e-13,
    0.567500, 6.46526e-13,
    0.568500, 6.22402e-13,
    0.569500, 6.41800e-13,
    0.570500, 6.12630e-13,
    0.571500, 6.33493e-13,
    0.572500, 6.59708e-13,
    0.573500, 6.56431e-13,
    0.574500, 6.55570e-13,
    0.575500, 6.44852e-13,
    0.576500, 6.52737e-13,
    0.577500, 6.58896e-13,
    0.578500, 6.34903e-13,
    0.579500, 6.53135e-13,
    0.580500, 6.58966e-13,
    0.581500, 6.66620e-13,
    0.582500, 6.76115e-13,
    0.583500, 6.72659e-13,
    0.584500, 6.76054e-13,
    0.585500, 6.50361e-13,
    0.586500, 6.69739e-13,
    0.587500, 6.78617e-13,
    0.588500, 6.44549e-13,
    0.589500, 5.95857e-13,
    0.590500, 6.72616e-13,
    0.591500, 6.65244e-13,
    0.592500, 6.75317e-13,
    0.593500, 6.73114e-13,
    0.594500, 6.66759e-13,
    0.595500, 6.72390e-13,
    0.596500, 6.83334e-13,
    0.597500, 6.76157e-13,
    0.598500, 6.69680e-13,
    0.599500, 6.78403e-13,
    0.600500, 6.69572e-13,
    0.601500, 6.73724e-13,
    0.602500, 6.63640e-13,
    0.603500, 6.92510e-13,
    0.604500, 6.90542e-13,
    0.605500, 6.87771e-13,
    0.606500, 6.88484e-13,
    0.607500, 6.89973e-13,
    0.608500, 6.86353e-13,
    0.609500, 6.89005e-13,
    0.610500, 6.75053e-13,
    0.611500, 6.94327e-13,
    0.612500, 6.80280e-13,
    0.613500, 6.73717e-13,
    0.614500, 6.87935e-13,
    0.615500, 6.90176e-13,
    0.616500, 6.50480e-13,
    0.617500, 6.92241e-13,
    0.618500, 7.01385e-13,
    0.619500, 6.96732e-13,
    0.620500, 7.10014e-13,
    0.621500, 6.94271e-13,
    0.622500, 7.05964e-13,
    0.623500, 6.88847e-13,
    0.624500, 6.86920e-13,
    0.625500, 6.79159e-13,
    0.626500, 7.08402e-13,
    0.627500, 7.10665e-13,
    0.628500, 7.12932e-13,
    0.629500, 7.06794e-13,
    0.631000, 6.94112e-13,
    0.633000, 7.03621e-13,
    0.635000, 7.10214e-13,
    0.637000, 7.13833e-13,
    0.639000, 7.17023e-13,
    0.641000, 7.05388e-13,
    0.643000, 7.12867e-13,
    0.645000, 7.19957e-13,
    0.647000, 7.13769e-13,
    0.649000, 6.98078e-13,
    0.651000, 7.23971e-13,
    0.653000, 7.25259e-13,
    0.655000, 6.99209e-13,
    0.657000, 6.35702e-13,
    0.659000, 7.15609e-13,
    0.661000, 7.30158e-13,
    0.663000, 7.27121e-13,
    0.665000, 7.33860e-13,
    0.667000, 7.26480e-13,
    0.669000, 7.36067e-13,
    0.671000, 7.26143e-13,
    0.673000, 7.32881e-13,
    0.675000, 7.31925e-13,
    0.677000, 7.35297e-13,
    0.679000, 7.34756e-13,
    0.681000, 7.36138e-13,
    0.683000, 7.34034e-13,
    0.685000, 7.26390e-13,
    0.687000, 7.36647e-13,
    0.689000, 7.37920e-13,
    0.691000, 7.35624e-13,
    0.693000, 7.39889e-13,
    0.695000, 7.38015e-13,
    0.697000, 7.31960e-13,
    0.699000, 7.40832e-13,
    0.701000, 7.24743e-13,
    0.703000, 7.29933e-13,
    0.705000, 7.48331e-13,
    0.707000, 7.44628e-13,
    0.709000, 7.40313e-13,
    0.711000, 7.45032e-13,
    0.713000, 7.42756e-13,
    0.715000, 7.43132e-13,
    0.717000, 7.40204e-13,
    0.719000, 7.30078e-13,
    0.721000, 7.35800e-13,
    0.723000, 7.49317e-13,
    0.725000, 7.54583e-13,
    0.727000, 7.56509e-13,
    0.729000, 7.45452e-13,
    0.731000, 7.53517e-13,
    0.733000, 7.53085e-13,
    0.735000, 7.52042e-13,
    0.737000, 7.54987e-13,
    0.739000, 7.42286e-13,
    0.741000, 7.34657e-13,
    0.743000, 7.55029e-13,
    0.745000, 7.54977e-13,
    0.747000, 7.61405e-13,
    0.749000, 7.57749e-13,
    0.751000, 7.57014e-13,
    0.753000, 7.59246e-13,
    0.755000, 7.60866e-13,
    0.757000, 7.60646e-13,
    0.759000, 7.59780e-13,
    0.761000, 7.61946e-13,
    0.763000, 7.68427e-13,
    0.765000, 7.60042e-13,
    0.767000, 7.41550e-13,
    0.769000, 7.56717e-13,
    0.771000, 7.61289e-13,
    0.773000, 7.67780e-13,
    0.775000, 7.59012e-13,
    0.777000, 7.68059e-13,
    0.779000, 7.66223e-13,
    0.781000, 7.70163e-13,
    0.783000, 7.66956e-13,
    0.785000, 7.73495e-13,
    0.787000, 7.75470e-13,
    0.789000, 7.77435e-13,
    0.791000, 7.70759e-13,
    0.793000, 7.64653e-13,
    0.795000, 7.62479e-13,
    0.797000, 7.78452e-13,
    0.799000, 7.70849e-13,
    0.801000, 7.79478e-13,
    0.803000, 7.74481e-13,
    0.805000, 7.68718e-13,
    0.807000, 7.75997e-13,
    0.809000, 7.62488e-13,
    0.811000, 7.79522e-13,
    0.813000, 7.84073e-13,
    0.815000, 7.82297e-13,
    0.817000, 7.84016e-13,
    0.819000, 7.58680e-13,
    0.821000, 7.74548e-13,
    0.823000, 7.73295e-13,
    0.825000, 7.78503e-13,
    0.827000, 7.83007e-13,
    0.829000, 7.83882e-13,
    0.831000, 7.84006e-13,
    0.833000, 7.62015e-13,
    0.835000, 7.79735e-13,
    0.837000, 7.82731e-13,
    0.839000, 7.79007e-13,
    0.841000, 7.84977e-13,
    0.843000, 7.75897e-13,
    0.845000, 7.83371e-13,
    0.847000, 7.80994e-13,
    0.849000, 7.43387e-13,
    0.851000, 7.71483e-13,
    0.853000, 7.51952e-13,
    0.855000, 6.81020e-13,
    0.857000, 7.88634e-13,
    0.859000, 7.81358e-13,
    0.861000, 7.85001e-13,
    0.863000, 7.90233e-13,
    0.865000, 7.70877e-13,
    0.867000, 7.02664e-13,
    0.869000, 7.75619e-13,
    0.870000, 7.70980e-13,
    0.872000, 7.68881e-13,
    0.874000, 7.74844e-13,
    0.876000, 7.80022e-13,
    0.878000, 7.63958e-13,
    0.880000, 7.68264e-13,
    0.882000, 7.61855e-13,
    0.884000, 7.76922e-13,
    0.886000, 7.67948e-13,
    0.888000, 7.73092e-13,
    0.890000, 7.73217e-13,
    0.892000, 7.69098e-13,
    0.894000, 7.75094e-13,
    0.896000, 7.82825e-13,
    0.898000, 7.64933e-13,
    0.900000, 7.64047e-13,
    0.902000, 7.69173e-13,
    0.904000, 7.63917e-13,
    0.906000, 7.67301e-13,
    0.908000, 7.47073e-13,
    0.910000, 7.60033e-13,
    0.912000, 7.70437e-13,
    0.914000, 7.66729e-13,
    0.916000, 7.65637e-13,
    0.918000, 7.69878e-13,
    0.920000, 7.49886e-13,
    0.922000, 7.46837e-13,
    0.924000, 7.55515e-13,
    0.926000, 7.63339e-13,
    0.928000, 7.72122e-13,
    0.930000, 7.70865e-13,
    0.932000, 7.81558e-13,
    0.934000, 7.72883e-13,
    0.936000, 7.62253e-13,
    0.938000, 7.72982e-13,
    0.940000, 7.69719e-13,
    0.942000, 7.58875e-13,
    0.944000, 7.77229e-13,
    0.946000, 7.75778e-13,
    0.948000, 7.63805e-13,
    0.950000, 7.68946e-13,
    0.952000, 7.65456e-13,
    0.954000, 7.58053e-13,
    0.956000, 7.74811e-13,
    0.958000, 7.75135e-13,
    0.960000, 7.70552e-13,
    0.962000, 7.69734e-13,
    0.964000, 7.70868e-13,
    0.966000, 7.64102e-13,
    0.968000, 7.71772e-13,
    0.970000, 7.70793e-13,
    0.972000, 7.78405e-13,
    0.974000, 7.63606e-13,
    0.976000, 7.73159e-13,
    0.978000, 7.71948e-13,
    0.980000, 7.71297e-13,
    0.982000, 7.77247e-13,
    0.984000, 7.74315e-13,
    0.986000, 7.73697e-13,
    0.988000, 7.74058e-13,
    0.990000, 7.65718e-13,
    0.992000, 7.75843e-13,
    0.994000, 7.77882e-13,
    0.996000, 7.76726e-13,
    0.998000, 7.77503e-13,
    1.00000, 7.77085e-13,
    1.00200, 7.77741e-13,
    1.00400, 7.63526e-13,
    1.00600, 7.40869e-13,
    1.00800, 7.74896e-13,
    1.01000, 7.76769e-13,
    1.01200, 7.75583e-13,
    1.01400, 7.71375e-13,
    1.01600, 7.68066e-13,
    1.01800, 7.68347e-13,
    1.02000, 7.67327e-13,
    1.02200, 7.66495e-13,
    1.02400, 7.76764e-13,
    1.02600, 7.76822e-13,
    1.02800, 7.78847e-13,
    1.03000, 7.70221e-13,
    1.03200, 7.75646e-13,
    1.03400, 7.58176e-13,
    1.03600, 7.73752e-13,
    1.03800, 7.65345e-13,
    1.04000, 7.67055e-13,
    1.04200, 7.69905e-13,
    1.04400, 7.75093e-13,
    1.04600, 7.60280e-13,
    1.04800, 7.68206e-13,
    1.05000, 7.72487e-13,
    1.05200, 7.71776e-13,
    1.05400, 7.67566e-13,
    1.05600, 7.73787e-13,
    1.05800, 7.56614e-13,
    1.06000, 7.61280e-13,
    1.06200, 7.71343e-13,
    1.06400, 7.65913e-13,
    1.06600, 7.60727e-13,
    1.06800, 7.56467e-13,
    1.07000, 7.47025e-13,
    1.07200, 7.61030e-13,
    1.07400, 7.52664e-13,
    1.07600, 7.54572e-13,
    1.07800, 7.52379e-13,
    1.08000, 7.67966e-13,
    1.08200, 7.35189e-13,
    1.08400, 7.48009e-13,
    1.08600, 7.64466e-13,
    1.08800, 7.29987e-13,
    1.09000, 7.59994e-13,
    1.09200, 7.54488e-13,
    1.09400, 7.10099e-13,
    1.09600, 7.31668e-13,
    1.09800, 7.32810e-13,
    1.10000, 7.53167e-13,
    1.10200, 7.39340e-13,
    1.10400, 7.50516e-13,
    1.10600, 7.52031e-13,
    1.10800, 7.51041e-13,
    1.11000, 7.53541e-13,
    1.11200, 7.45236e-13,
    1.11400, 7.48728e-13,
    1.11600, 7.52343e-13,
    1.11800, 7.51935e-13,
    1.12000, 7.39024e-13,
    1.12200, 7.53811e-13,
    1.12400, 7.51976e-13,
    1.12600, 7.35279e-13,
    1.12800, 7.48094e-13,
    1.13000, 7.39450e-13,
    1.13200, 7.46645e-13,
    1.13400, 7.44080e-13,
    1.13600, 7.52130e-13,
    1.13800, 7.38265e-13,
    1.14000, 7.34401e-13,
    1.14200, 7.40252e-13,
    1.14400, 7.41946e-13,
    1.14600, 7.54398e-13,
    1.14800, 7.51080e-13,
    1.15000, 7.51305e-13,
    1.15200, 7.49650e-13,
    1.15400, 7.55196e-13,
    1.15600, 7.50879e-13,
    1.15800, 7.52035e-13,
    1.16000, 7.37603e-13,
    1.16200, 7.30451e-13,
    1.16400, 7.40477e-13,
    1.16600, 7.42897e-13,
    1.16800, 7.48293e-13,
    1.17000, 7.38459e-13,
    1.17200, 7.51396e-13,
    1.17400, 7.52896e-13,
    1.17600, 7.34453e-13,
    1.17800, 7.32650e-13,
    1.18000, 7.53040e-13,
    1.18200, 7.44843e-13,
    1.18400, 7.22246e-13,
    1.18600, 7.47360e-13,
    1.18800, 7.24513e-13,
    1.19000, 7.41124e-13,
    1.19200, 7.49974e-13,
    1.19400, 7.51226e-13,
    1.19600, 7.42256e-13,
    1.19800, 7.10901e-13,
    1.20000, 7.32947e-13,
    1.20200, 7.49770e-13,
    1.20400, 7.21925e-13,
    1.20600, 7.46362e-13,
    1.20800, 7.14375e-13,
    1.21000, 7.32725e-13,
    1.21200, 7.43239e-13,
    1.21400, 7.46823e-13,
    1.21600, 7.49254e-13,
    1.21800, 7.46965e-13,
    1.22000, 7.45715e-13,
    1.22200, 7.45989e-13,
    1.22400, 7.44534e-13,
    1.22600, 7.45692e-13,
    1.22800, 7.36164e-13,
    1.23000, 7.45193e-13,
    1.23200, 7.41753e-13,
    1.23400, 7.43028e-13,
    1.23600, 7.44193e-13,
    1.23800, 7.46781e-13,
    1.24000, 7.38000e-13,
    1.24200, 7.38378e-13,
    1.24400, 7.37365e-13,
    1.24600, 7.41591e-13,
    1.24800, 7.42417e-13,
    1.25000, 7.44604e-13,
    1.25200, 7.35462e-13,
    1.25400, 7.40681e-13,
    1.25600, 7.38137e-13,
    1.25800, 7.37776e-13,
    1.26000, 7.40341e-13,
    1.26200, 7.37112e-13,
    1.26400, 7.37111e-13,
    1.26600, 7.36791e-13,
    1.26800, 7.27618e-13,
    1.27000, 7.40958e-13,
    1.27200, 7.40272e-13,
    1.27400, 7.35379e-13,
    1.27600, 7.40361e-13,
    1.27800, 7.38387e-13,
    1.28000, 7.28681e-13,
    1.28200, 6.54730e-13,
    1.28400, 7.18978e-13,
    1.28600, 7.29205e-13,
    1.28800, 7.32614e-13,
    1.29000, 7.27365e-13,
    1.29200, 7.34588e-13,
    1.29400, 7.31495e-13,
    1.29600, 7.37546e-13,
    1.29800, 7.31092e-13,
    1.30000, 7.36586e-13,
    1.30200, 7.29567e-13,
    1.30400, 7.26690e-13,
    1.30600, 7.34370e-13,
    1.30800, 7.33400e-13,
    1.31000, 7.32505e-13,
    1.31200, 7.16767e-13,
    1.31400, 7.32099e-13,
    1.31600, 7.11538e-13,
    1.31800, 7.28914e-13,
    1.32000, 7.33202e-13,
    1.32200, 7.29788e-13,
    1.32400, 7.32798e-13,
    1.32600, 7.28077e-13,
    1.32800, 7.28023e-13,
    1.33000, 7.15809e-13,
    1.33200, 7.18618e-13,
    1.33400, 7.32919e-13,
    1.33600, 7.29491e-13,
    1.33800, 7.27149e-13,
    1.34000, 7.19411e-13,
    1.34200, 7.27608e-13,
    1.34400, 7.29677e-13,
    1.34600, 7.26449e-13,
    1.34800, 7.30018e-13,
    1.35000, 7.20116e-13,
    1.35200, 7.28502e-13,
    1.35400, 7.27629e-13,
    1.35600, 7.09621e-13,
    1.35800, 7.25615e-13,
    1.36000, 7.17495e-13,
    1.36200, 7.24479e-13,
    1.36400, 7.17437e-13,
    1.36600, 7.24926e-13,
    1.36800, 7.15838e-13,
    1.37000, 7.14058e-13,
    1.37200, 7.21997e-13,
    1.37400, 7.20119e-13,
    1.37600, 7.12581e-13,
    1.37800, 7.22109e-13,
    1.38000, 7.22719e-13,
    1.38200, 7.16327e-13,
    1.38400, 7.23254e-13,
    1.38600, 7.16321e-13,
    1.38800, 7.22771e-13,
    1.39000, 7.17933e-13,
    1.39200, 7.22498e-13,
    1.39400, 7.19660e-13,
    1.39600, 7.18153e-13,
    1.39800, 7.23402e-13,
    1.40000, 7.09560e-13,
    1.40200, 7.14030e-13,
    1.40400, 7.11328e-13,
    1.40600, 7.12893e-13,
    1.40800, 7.16188e-13,
    1.41000, 7.17706e-13,
    1.41200, 7.01446e-13,
    1.41400, 7.05653e-13,
    1.41600, 7.13299e-13,
    1.41800, 7.14400e-13,
    1.42000, 7.09634e-13,
    1.42200, 6.94749e-13,
    1.42400, 7.05456e-13,
    1.42600, 6.95005e-13,
    1.42800, 6.95410e-13,
    1.43000, 7.00601e-13,
    1.43200, 7.05738e-13,
    1.43400, 7.05736e-13,
    1.43600, 7.09899e-13,
    1.43800, 7.13036e-13,
    1.44000, 6.83420e-13,
    1.44200, 6.97987e-13,
    1.44400, 6.93385e-13,
    1.44600, 7.08350e-13,
    1.44800, 7.04322e-13,
    1.45000, 7.00715e-13,
    1.45200, 6.93039e-13,
    1.45400, 6.94802e-13,
    1.45600, 6.93813e-13,
    1.45800, 7.07452e-13,
    1.46000, 7.04405e-13,
    1.46200, 6.98032e-13,
    1.46400, 6.98972e-13,
    1.46600, 6.96551e-13,
    1.46800, 7.00362e-13,
    1.47000, 6.97267e-13,
    1.47200, 6.95181e-13,
    1.47400, 6.86028e-13,
    1.47600, 6.89137e-13,
    1.47800, 6.85748e-13,
    1.48000, 7.01278e-13,
    1.48200, 6.97518e-13,
    1.48400, 6.89143e-13,
    1.48600, 6.97572e-13,
    1.48800, 6.45399e-13,
    1.49000, 7.01932e-13,
    1.49200, 6.98762e-13,
    1.49400, 7.05557e-13,
    1.49600, 6.86136e-13,
    1.49800, 6.97511e-13,
    1.50000, 6.98205e-13,
    1.50200, 6.71491e-13,
    1.50400, 6.63009e-13,
    1.50600, 6.58236e-13,
    1.50800, 6.82318e-13,
    1.51000, 7.02941e-13,
    1.51200, 6.91403e-13,
    1.51400, 6.87744e-13,
    1.51600, 6.92874e-13,
    1.51800, 6.96682e-13,
    1.52000, 6.95945e-13,
    1.52200, 6.78982e-13,
    1.52400, 6.85717e-13,
    1.52600, 6.97169e-13,
    1.52800, 7.00251e-13,
    1.53000, 6.72957e-13,
    1.53200, 6.96530e-13,
    1.53400, 6.85148e-13,
    1.53600, 6.96404e-13,
    1.53800, 6.90052e-13,
    1.54000, 6.77828e-13,
    1.54200, 6.86078e-13,
    1.54400, 6.97590e-13,
    1.54600, 6.98047e-13,
    1.54800, 6.80357e-13,
    1.55000, 6.80521e-13,
    1.55200, 6.91451e-13,
    1.55400, 6.71547e-13,
    1.55600, 6.78804e-13,
    1.55800, 6.83176e-13,
    1.56000, 6.82619e-13,
    1.56200, 6.88693e-13,
    1.56400, 6.82395e-13,
    1.56600, 6.74025e-13,
    1.56800, 6.72402e-13,
    1.57000, 6.77539e-13,
    1.57200, 6.82788e-13,
    1.57400, 6.69961e-13,
    1.57600, 6.48635e-13,
    1.57800, 6.42191e-13,
    1.58000, 6.82538e-13,
    1.58200, 6.59314e-13,
    1.58400, 6.70182e-13,
    1.58600, 6.73788e-13,
    1.58800, 6.45933e-13,
    1.59000, 6.16510e-13,
    1.59200, 6.58976e-13,
    1.59400, 6.81467e-13,
    1.59600, 6.55355e-13,
    1.59800, 6.83954e-13,
    1.60000, 6.65312e-13,
    1.60200, 6.67991e-13,
    1.60400, 6.68640e-13,
    1.60600, 6.66424e-13,
    1.60800, 6.74217e-13,
    1.61000, 6.43323e-13,
    1.61200, 6.59802e-13,
    1.61400, 6.68733e-13,
    1.61600, 6.37973e-13,
    1.61800, 6.71160e-13,
    1.62000, 6.46681e-13,
    1.62200, 6.61522e-13,
    1.62400, 6.71745e-13,
    1.62600, 6.70677e-13,
    1.62800, 6.78164e-13,
    1.63000, 6.68887e-13,
    1.63200, 6.67216e-13,
    1.63400, 6.60924e-13,
    1.63600, 6.54317e-13,
    1.63800, 6.36776e-13,
    1.64000, 6.36171e-13,
    1.64200, 6.36295e-13,
    1.64400, 6.36740e-13,
    1.64600, 6.55151e-13,
    1.64800, 6.57653e-13,
    1.65000, 6.45953e-13,
    1.65200, 6.49024e-13,
    1.65400, 6.56352e-13,
    1.65600, 6.57130e-13,
    1.65800, 6.58138e-13,
    1.66000, 6.52600e-13,
    1.66200, 6.56297e-13,
    1.66400, 6.53466e-13,
    1.66600, 6.44878e-13,
    1.66800, 6.36959e-13,
    1.67000, 6.54164e-13,
    1.67200, 6.28981e-13,
    1.67400, 6.44757e-13,
    1.67600, 6.25197e-13,
    1.67800, 6.36140e-13,
    1.68000, 6.08532e-13,
    1.68200, 5.99633e-13,
    1.68400, 6.29073e-13,
    1.68600, 6.32920e-13,
    1.68800, 6.33499e-13,
    1.69000, 6.29329e-13,
    1.69200, 6.41040e-13,
    1.69400, 6.38429e-13,
    1.69600, 6.37710e-13,
    1.69800, 6.36531e-13,
    1.70000, 6.27541e-13,
    1.70200, 6.24004e-13,
    1.70400, 6.26401e-13,
    1.70600, 6.28900e-13,
    1.70800, 6.19666e-13,
    1.71000, 6.25262e-13,
    1.71200, 6.01648e-13,
    1.71400, 6.30154e-13,
    1.71600, 6.24652e-13,
    1.71800, 6.23657e-13,
    1.72000, 6.15724e-13,
    1.72200, 6.16649e-13,
    1.72400, 5.97561e-13,
    1.72600, 6.11763e-13,
    1.72800, 6.10277e-13,
    1.73000, 6.15037e-13,
    1.73200, 6.04261e-13,
    1.73400, 5.75066e-13,
    1.73600, 5.61680e-13,
    1.73800, 5.82457e-13,
    1.74000, 5.99830e-13,
    1.74200, 5.95712e-13,
    1.74400, 6.06618e-13,
    1.74600, 5.95533e-13,
    1.74800, 5.94371e-13,
    1.75000, 5.97109e-13,
    1.75200, 5.95446e-13,
    1.75400, 6.03188e-13,
    1.75600, 6.01572e-13,
    1.75800, 6.01717e-13,
    1.76000, 6.00923e-13,
    1.76200, 5.85140e-13,
    1.76400, 5.95785e-13,
    1.76600, 6.00909e-13,
    1.76800, 5.95708e-13,
    1.77000, 5.92095e-13,
    1.77200, 5.95963e-13,
    1.77400, 5.97032e-13,
    1.77600, 5.86732e-13,
    1.77800, 5.83875e-13,
    1.78000, 5.86063e-13,
    1.78200, 5.85395e-13,
    1.78400, 5.85874e-13,
    1.78600, 5.83927e-13,
    1.78800, 5.91676e-13,
    1.79000, 5.87261e-13,
    1.79200, 5.84003e-13,
    1.79400, 5.80302e-13,
    1.79600, 5.81186e-13,
    1.79800, 5.81319e-13,
    1.80000, 5.79641e-13,
    1.80200, 5.70133e-13,
    1.80400, 5.78704e-13,
    1.80600, 5.76185e-13,
    1.80800, 5.76595e-13,
    1.81000, 5.76716e-13,
    1.81200, 5.71652e-13,
    1.81400, 5.66361e-13,
    1.81600, 5.52284e-13,
    1.81800, 5.13590e-13,
    1.82000, 5.50944e-13,
    1.82200, 5.47623e-13,
    1.82400, 5.65915e-13,
    1.82600, 5.66850e-13,
    1.82800, 5.60324e-13,
    1.83000, 5.66457e-13,
    1.83200, 5.62532e-13,
    1.83400, 5.60541e-13,
    1.83600, 5.61536e-13,
    1.83800, 5.55460e-13,
    1.84000, 5.57606e-13,
    1.84200, 5.47818e-13,
    1.84400, 5.53545e-13,
    1.84600, 5.58365e-13,
    1.84800, 5.36435e-13,
    1.85000, 5.58834e-13,
    1.85200, 5.55610e-13,
    1.85400, 5.52216e-13,
    1.85600, 5.44047e-13,
    1.85800, 5.51977e-13,
    1.86000, 5.43388e-13,
    1.86200, 5.40151e-13,
    1.86400, 5.43588e-13,
    1.86600, 5.35598e-13,
    1.86800, 5.36669e-13,
    1.87000, 5.42668e-13,
    1.87200, 5.26123e-13,
    1.87400, 5.12178e-13,
    1.87600, 4.46945e-13,
    1.87800, 5.23286e-13,
    1.88000, 5.29141e-13,
    1.88200, 5.37328e-13,
    1.88400, 5.35457e-13,
    1.88600, 5.25875e-13,
    1.88800, 5.38056e-13,
    1.89000, 5.24510e-13,
    1.89200, 5.23547e-13,
    1.89400, 5.18181e-13,
    1.89600, 5.08546e-13,
    1.89800, 5.27070e-13,
    1.90000, 5.24053e-13,
    1.90200, 5.36481e-13,
    1.90400, 5.25945e-13,
    1.90600, 5.29258e-13,
    1.90800, 5.25797e-13,
    1.91000, 5.30504e-13,
    1.91200, 5.19116e-13,
    1.91400, 5.29884e-13,
    1.91600, 5.25962e-13,
    1.91800, 5.24187e-13,
    1.92000, 5.15858e-13,
    1.92200, 5.26272e-13,
    1.92400, 5.19278e-13,
    1.92600, 5.23667e-13,
    1.92800, 5.11027e-13,
    1.93000, 5.10823e-13,
    1.93200, 5.05342e-13,
    1.93400, 5.14171e-13,
    1.93600, 5.13959e-13,
    1.93800, 5.16829e-13,
    1.94000, 5.00300e-13,
    1.94200, 5.07327e-13,
    1.94400, 4.64664e-13,
    1.94600, 4.59172e-13,
    1.94800, 5.00963e-13,
    1.95000, 5.01190e-13,
    1.95200, 4.87167e-13,
    1.95400, 5.12530e-13,
    1.95600, 5.10517e-13,
    1.95800, 5.10310e-13,
    1.96000, 5.07188e-13,
    1.96200, 5.03740e-13,
    1.96400, 4.89288e-13,
    1.96600, 4.98149e-13,
    1.96800, 5.08054e-13,
    1.97000, 5.04290e-13,
    1.97200, 4.89168e-13,
    1.97400, 4.98210e-13,
    1.97600, 5.02646e-13,
    1.97800, 4.88209e-13,
    1.98000, 4.93516e-13,
    1.98200, 4.94868e-13,
    1.98400, 4.95495e-13,
    1.98600, 4.81433e-13,
    1.98800, 5.00503e-13,
    1.99000, 4.99770e-13,
    1.99200, 4.92971e-13,
    1.99400, 4.84237e-13,
    1.99600, 4.92170e-13,
    1.99800, 4.87685e-13,
    2.00000, 4.94915e-13,
    2.00200, 4.90296e-13,
    2.00400, 4.87558e-13,
    2.00600, 4.86984e-13,
    2.00800, 4.92660e-13,
    2.01000, 4.91268e-13,
    2.01200, 4.89777e-13,
    2.01400, 4.87242e-13,
    2.01600, 4.88962e-13,
    2.01800, 4.88320e-13,
    2.02000, 4.82207e-13,
    2.02200, 4.73967e-13,
    2.02400, 4.82121e-13,
    2.02600, 4.83177e-13,
    2.02800, 4.80140e-13,
    2.03000, 4.69698e-13,
    2.03200, 4.82197e-13,
    2.03400, 4.75758e-13,
    2.03600, 4.75972e-13,
    2.03800, 4.63999e-13,
    2.04000, 4.78615e-13,
    2.04200, 4.75565e-13,
    2.04400, 4.78015e-13,
    2.04600, 4.77576e-13,
    2.04800, 4.74283e-13,
    2.05000, 4.74405e-13,
    2.05200, 4.68979e-13,
    2.05400, 4.71633e-13,
    2.05600, 4.72506e-13,
    2.05800, 4.70368e-13,
    2.06000, 4.61923e-13,
    2.06200, 4.71428e-13,
    2.06400, 4.53109e-13,
    2.06600, 4.69738e-13,
    2.06800, 4.67044e-13,
    2.07000, 4.58812e-13,
    2.07200, 4.63702e-13,
    2.07400, 4.66966e-13,
    2.07600, 4.66063e-13,
    2.07800, 4.65679e-13,
    2.08000, 4.55948e-13,
    2.08200, 4.62139e-13,
    2.08400, 4.54139e-13,
    2.08600, 4.61937e-13,
    2.08800, 4.60898e-13,
    2.09000, 4.61020e-13,
    2.09200, 4.46627e-13,
    2.09400, 4.51786e-13,
    2.09600, 4.50793e-13,
    2.09800, 4.54576e-13,
    2.10000, 4.55058e-13,
    2.10200, 4.54163e-13,
    2.10400, 4.55588e-13,
    2.10600, 4.56493e-13,
    2.10800, 4.54663e-13,
    2.11000, 4.46787e-13,
    2.11200, 4.52948e-13,
    2.11400, 4.51579e-13,
    2.11600, 4.43895e-13,
    2.11800, 4.49794e-13,
    2.12000, 4.45070e-13,
    2.12200, 4.47130e-13,
    2.12400, 4.40436e-13,
    2.12600, 4.43971e-13,
    2.12800, 4.47359e-13,
    2.13000, 4.45428e-13,
    2.13200, 4.46850e-13,
    2.13400, 4.45599e-13,
    2.13600, 4.36500e-13,
    2.13800, 4.44875e-13,
    2.14000, 4.42963e-13,
    2.14200, 4.42987e-13,
    2.14400, 4.40377e-13,
    2.14600, 4.37239e-13,
    2.14800, 4.41022e-13,
    2.15000, 4.40132e-13,
    2.15200, 4.37460e-13,
    2.15400, 4.37087e-13,
    2.15600, 4.37303e-13,
    2.15800, 4.36489e-13,
    2.16000, 4.33322e-13,
    2.16200, 4.29252e-13,
    2.16400, 4.20974e-13,
    2.16600, 3.78746e-13,
    2.16800, 4.14123e-13,
    2.17000, 4.25559e-13,
    2.17200, 4.28047e-13,
    2.17400, 4.29030e-13,
    2.17600, 4.25064e-13,
    2.17800, 4.18623e-13,
    2.18000, 4.30053e-13,
    2.18200, 4.21488e-13,
    2.18400, 4.27992e-13,
    2.18600, 4.28594e-13,
    2.18800, 4.14800e-13,
    2.19000, 4.23539e-13,
    2.19200, 4.26734e-13,
    2.19400, 4.25392e-13,
    2.19600, 4.24615e-13,
    2.19800, 4.25316e-13,
    2.20000, 4.23993e-13,
    2.20200, 4.22401e-13,
    2.20400, 4.23343e-13,
    2.20600, 4.01944e-13,
    2.20800, 4.12401e-13,
    2.21000, 4.20265e-13,
    2.21200, 4.20399e-13,
    2.21400, 4.19323e-13,
    2.21600, 4.15336e-13,
    2.21800, 4.15640e-13,
    2.22000, 4.18398e-13,
    2.22200, 4.16883e-13,
    2.22400, 4.15840e-13,
    2.22600, 4.07600e-13,
    2.22800, 4.13185e-13,
    2.23000, 4.13555e-13,
    2.23200, 4.13935e-13,
    2.23400, 4.14172e-13,
    2.23600, 4.12628e-13,
    2.23800, 4.04914e-13,
    2.24000, 4.08110e-13,
    2.24200, 4.08163e-13,
    2.24400, 4.09332e-13,
    2.24600, 4.09809e-13,
    2.24800, 4.02980e-13,
    2.25000, 4.07687e-13,
    2.25200, 4.06088e-13,
    2.25400, 3.99432e-13,
    2.25600, 4.03032e-13,
    2.25800, 4.05353e-13,
    2.26000, 4.05240e-13,
    2.26200, 3.96348e-13,
    2.26400, 4.02010e-13,
    2.26600, 3.99723e-13,
    2.26800, 4.02059e-13,
    2.27000, 4.01889e-13,
    2.27200, 3.99818e-13,
    2.27400, 3.98066e-13,
    2.27600, 4.00711e-13,
    2.27800, 4.00697e-13,
    2.28000, 3.99013e-13,
    2.28200, 3.82156e-13,
    2.28400, 3.95939e-13,
    2.28600, 3.94788e-13,
    2.28800, 3.96657e-13,
    2.29000, 3.96396e-13,
    2.29200, 3.95144e-13,
    2.29400, 3.81872e-13,
    2.29600, 3.85539e-13,
    2.29800, 3.85464e-13,
    2.30000, 3.88166e-13,
    2.30200, 3.89663e-13,
    2.30400, 3.89708e-13,
    2.30600, 3.89602e-13,
    2.30800, 3.89369e-13,
    2.31000, 3.87762e-13,
    2.31200, 3.87987e-13,
    2.31400, 3.88549e-13,
    2.31600, 3.83863e-13,
    2.31800, 3.80911e-13,
    2.32000, 3.85783e-13,
    2.32200, 3.78113e-13,
    2.32400, 3.70837e-13,
    2.32600, 3.71319e-13,
    2.32800, 3.78927e-13,
    2.33000, 3.80441e-13,
    2.33200, 3.76653e-13,
    2.33400, 3.79304e-13,
    2.33600, 3.74665e-13,
    2.33800, 3.73766e-13,
    2.34000, 3.79136e-13,
    2.34200, 3.79169e-13,
    2.34400, 3.78885e-13,
    2.34600, 3.77304e-13,
    2.34800, 3.77992e-13,
    2.35000, 3.78001e-13,
    2.35200, 3.63148e-13,
    2.35400, 3.62496e-13,
    2.35600, 3.69338e-13,
    2.35800, 3.64649e-13,
    2.36000, 3.69969e-13,
    2.36200, 3.71970e-13,
    2.36400, 3.70799e-13,
    2.36600, 3.70861e-13,
    2.36800, 3.70827e-13,
    2.37000, 3.66784e-13,
    2.37200, 3.69144e-13,
    2.37400, 3.56081e-13,
    2.37600, 3.67741e-13,
    2.37800, 3.70410e-13,
    2.38000, 3.69127e-13,
    2.38200, 3.65147e-13,
    2.38400, 3.46836e-13,
    2.38600, 3.47862e-13,
    2.38800, 3.60854e-13,
    2.39000, 3.62207e-13,
    2.39200, 3.60859e-13,
    2.39400, 3.61537e-13,
    2.39600, 3.60933e-13,
    2.39800, 3.63447e-13,
    2.40000, 3.58613e-13,
    2.40200, 3.62200e-13,
    2.40400, 3.61443e-13,
    2.40600, 3.60373e-13,
    2.40800, 3.60272e-13,
    2.41000, 3.60351e-13,
    2.41200, 3.60728e-13,
    2.41400, 3.45870e-13,
    2.41600, 3.36563e-13,
    2.41800, 3.54201e-13,
    2.42000, 3.52558e-13,
    2.42200, 3.54307e-13,
    2.42400, 3.52192e-13,
    2.42600, 3.52508e-13,
    2.42800, 3.52698e-13,
    2.43000, 3.54692e-13,
    2.43200, 3.53261e-13,
    2.43400, 3.50906e-13,
    2.43600, 3.47889e-13,
    2.43800, 3.48242e-13,
    2.44000, 3.52491e-13,
    2.44200, 3.51656e-13,
    2.44400, 3.51277e-13,
    2.44600, 3.43920e-13,
    2.44800, 3.41251e-13,
    2.45000, 3.40821e-13,
    2.45200, 3.40944e-13,
    2.45400, 3.45357e-13,
    2.45600, 3.39709e-13,
    2.45800, 3.36053e-13,
    2.46000, 3.46337e-13,
    2.46200, 3.45695e-13,
    2.46400, 3.46047e-13,
    2.46600, 3.44790e-13,
    2.46800, 3.44971e-13,
    2.47000, 3.34644e-13,
    2.47200, 3.44618e-13,
    2.47400, 3.38220e-13,
    2.47600, 3.43582e-13,
    2.47800, 3.41573e-13,
    2.48000, 3.27900e-13,
    2.48200, 3.28511e-13,
    2.48400, 3.39852e-13,
    2.48600, 3.27966e-13,
    2.48800, 3.38553e-13,
    2.49000, 3.39015e-13,
    2.49200, 3.38429e-13,
    2.49400, 3.35157e-13,
    2.49600, 3.36748e-13,
    2.49800, 3.35981e-13,
    2.50000, 3.37610e-13
])
COLINA_ARRAY = COLINA_ARRAY.reshape(COLINA_ARRAY.size//2, 2)

COLINA_WAVELENGTH_MICRON = COLINA_ARRAY[:, 0]
COLINA_FLUX_PER_HZ = COLINA_ARRAY[:, 1] * np.pi  # Column is F, not pi*F

FLUX_DENSITY = tab.Tabulation(COLINA_WAVELENGTH_MICRON, COLINA_FLUX_PER_HZ)
UNITS = 'W/m^2/Hz'
XUNITS = 'um'

################################################################################
