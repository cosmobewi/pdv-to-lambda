===========================
Dynamique avec échange : Q
===========================

Principe et conservation
------------------------

On conserve l’énergie-matière totale mais on autorise un **échange homogène**
entre rayonnement et vide :

.. math::
   \dot\rho_r + 4H\rho_r = -Q, \qquad
   \dot\rho_m + 3H\rho_m = 0, \qquad
   \dot\rho_\Lambda = +Q.

**Choix minimal pour la source.**

.. math::
   Q(a) = \eta(a)\,H\,\rho_r.

- **Dimensionnellement naturel** : :math:`Q` a les dimensions d’une densité/temps.
- **S’éteint si l’expansion s’arrête** (:math:`H\to0`), et suit l’« énergie disponible »
  (:math:`\rho_r`), cible logique du terme :math:`p\,dV`.
- **Standard en cosmologie couplée** : forme simple, bien posée numériquement.

Paramétrisation lisse (fenêtre tardive)
---------------------------------------

On cherche une efficacité **croissante** avec l’expansion (pondération par volume comobile)
et une **mise en route douce** autour de :math:`a_\star` :

.. math::
   \eta(a) \;=\; \eta_0\,a^3 \;
   \frac{1+\tanh\!\big(\frac{a-a_\star}{\Delta}\big)}{2}.
   \tag{1}

- Le facteur :math:`a^3` implémente la pondération « volume comobile ».
- La **tanh** évite les angles vifs (meilleure stabilité numérique).
- :math:`\Delta` contrôle la largeur de la transition (ex. :math:`\Delta\sim 0.05` en unités de :math:`a`).

.. note::
   **Normalisation.** Si tu préfères normaliser l’efficacité à l’instant d’activation,
   tu peux poser :math:`\eta(a)=\bar\eta_0\,(a/a_\star)^3 \times \text{tanh-window}`.
   Dans ce cas, la loi intégrée ci-dessous s’écrit avec :math:`\eta_0 \equiv \bar\eta_0\,a_\star^{-3}`.
   La forme (1) évite d’avoir à re-traiter ce facteur.

Intégration (fond)
------------------

**Pourquoi la relation suivante ?**

.. math::
   :name: eq:OmegaLambda-linear

   \Omega_{\Lambda 0} \simeq \eta_0\,\Omega_{r0}\,z_\star
   
À partir de :math:`\dot\rho_\Lambda=Q`, on obtient

.. math::
   \frac{d\rho_\Lambda}{d\ln a} \;=\; \eta(a)\,\rho_r(a).

En utilisant :math:`\rho_r(a)=\rho_{r0}\,a^{-4}` (approximation « rétro-action faible »
suffisante pour un ordre de grandeur) et la forme (1) avec une fenêtre qui passe
rapidement à 1 après :math:`a_\star` :

.. math::
   \rho_{\Lambda 0}
   \simeq
   \eta_0\,\rho_{r0}\int_{\ln a_\star}^{0}\! a^3\,a^{-4}\; d\ln a
   \;=\;
   \eta_0\,\rho_{r0}\!\int_{a_\star}^{1}\!\frac{da}{a^2}
   \;=\;
   \eta_0\,\rho_{r0}\,\big(a_\star^{-1}-1\big)
   \;=\;
   \eta_0\,\rho_{r0}\,z_\star.

En divisant par :math:`\rho_{c0}` :

.. math::
   \Omega_{\Lambda 0} \;\simeq\; \eta_0\,\Omega_{r0}\,z_\star.
   \tag{2}

Cette relation **linéaire en :math:`z_\star`** est la traduction directe de la
pondération :math:`a^3` (volume comobile) et du fait que :math:`\rho_r\propto a^{-4}`.

État effectif du vide (lecture observationnelle)
------------------------------------------------

On peut regrouper le terme d’échange dans un **état d’équation effectif** :

.. math::
   \frac{d\rho_\Lambda}{d\ln a} = -3\,(1+w_\Lambda^{\rm eff})\,\rho_\Lambda
   \qquad\Rightarrow\qquad
   w_\Lambda^{\rm eff}(a) = -1 - \frac{Q}{3H\rho_\Lambda}
   = -1 - \frac{\eta(a)\,\rho_r}{3\,\rho_\Lambda}.
   \tag{3}

Aujourd’hui,

.. math::
   |w_0+1| \;=\; \frac{\eta(a_0)}{3}\,\frac{\rho_{r0}}{\rho_{\Lambda0}}
   \;\approx\; \frac{\eta_0}{3}\,\frac{\Omega_{r0}}{\Omega_{\Lambda0}}
   \;\sim\; 10^{-4}\,\eta_0,

car :math:`\Omega_{r0}/\Omega_{\Lambda0}\simeq 9\times10^{-5}/0.69 \approx 1.3\times10^{-4}`.
Le signal est donc **phantom-like** mais **extrêmement proche de -1**, bien au-delà
de la précision actuelle.

Signes, cohérence et contraintes
--------------------------------

- **Signe de :math:`Q`** : ici :math:`Q>0` (le vide gagne de l’énergie, le rayonnement
  se vide plus vite). La somme est conservée par construction.
- **Matière non affectée** au fond (:math:`\dot\rho_m+3H\rho_m=0`) : c’est un choix
  minimal qui évite de perturber BBN/CMB via la densité baryonique ou la croissance
  de structure à haut :math:`z`.
- **Spectre CMB & distorsions** : si la fenêtre s’active **après recombinaison**
  (ou très doucement avant), la variation de :math:`\rho_r` reste assez faible pour
  ne pas contredire les contraintes de type FIRAS (ordre :math:`10^{-5}` sur les
  distorsions). Cela fixe pratiquement :math:`a_\star` et :math:`\Delta` à tester
  numériquement.
- **Stabilité** : l’« état phantom » est ici **effectif**, dû au transfert ;
  on ne postule pas de champ fantôme (pas de pathologie du Lagrangien).
- **Monotonicité** : avec :math:`\eta(a)\ge 0`, on a :math:`\dot\rho_\Lambda\ge 0`,
  :math:`\rho_\Lambda` croît et reste positive.

À retenir
---------

- Le couplage :math:`Q=\eta(a)H\rho_r` est le **ansatz minimal** qui implémente
  l’idée « une fraction du travail :math:`p\,dV` du rayonnement alimente le vide ».
- La pondération :math:`a^3` + fenêtre tanh donne naturellement (2), simple et
  **prédictive** : l’ordre de grandeur de \ :math:`\eta_0` se lit directement
  sur :math:`\Omega_{\Lambda0}/(\Omega_{r0} z_\star)`.
- Le décalage de :math:`w_\Lambda^{\rm eff}` par rapport à :math:`-1` est
  de l’ordre :math:`10^{-4}\eta_0` aujourd’hui : **indétectable** pour l’instant,
  mais traçable dans une analyse conjointe fond + perturbations (ISW tardif, RSD).