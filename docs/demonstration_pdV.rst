========================================
Démonstration : « conversion p dV → Λ »
========================================

Cadre
-----

    - On travaille dans un Univers FLRW homogène et isotrope. 
    - Dans une cellule **comobile** (volume physique :math:`V=a^3 V_c`), 
    - on suit séparément le rayonnement (:math:`\gamma`) et le vide (:math:`\Lambda`).

Définitions & rappel
-----------------------

- Énergie contenue : :math:`U_i = \rho_i\,a^3 V_c`.
- Travail élémentaire : :math:`\delta W = p\,dV = p\,d(a^3 V_c)`.
- Rayonnement : :math:`p_\gamma = \tfrac{1}{3}\rho_\gamma`, :math:`\rho_\gamma \propto a^{-4}` (si non couplé).

Postulat de conversion locale
--------------------------------

On **postule** qu’une fraction constante :math:`\eta` du travail instantané du
rayonnement est **captée par le vide** :

.. math::
   dU_\Lambda \;=\; \eta\, p_\gamma\, dV
   \qquad\Longleftrightarrow\qquad
   d(\rho_\Lambda a^3) \;=\; \eta\, p_\gamma\, d(a^3).

En insérant :math:`p_\gamma=\tfrac{1}{3}\rho_\gamma` :

.. math::
   d(\rho_\Lambda a^3) \;=\; \frac{\eta}{3}\,\rho_\gamma\, d(a^3). \tag{A}

**Interprétation « source »** (équations de continuité couplées).
En dérivant par le temps et en notant :math:`H=\dot a/a` :

.. math::
   \dot\rho_\Lambda
   \;=\;
   \eta\, H\,\rho_\gamma,
   \qquad
   \dot\rho_\gamma + 4H\rho_\gamma
   \;=\;
   -\,\eta\, H\,\rho_\gamma. \tag{B}

Ici, :math:`Q\equiv \eta H\rho_\gamma` est le **taux de transfert par unité de volume**
(positif vers le vide). La somme respecte bien la conservation totale
:math:`\dot\rho_\text{tot}+3H(\rho_\text{tot}+p_\text{tot})=0`.

Formule « maître » (intégrale générale)
------------------------------------------

En intégrant (A) de :math:`a_\star` (début du processus) à :math:`a` :

.. math::
   \rho_\Lambda(a) a^3 - \rho_\Lambda(a_\star) a_\star^3
   \;=\;
   \frac{\eta}{3}\int_{a_\star}^{a} \rho_\gamma(a')\, d(a'^3).

Si l’on prend :math:`\rho_\Lambda(a_\star)\simeq 0` et que l’on évalue **aujourd’hui**
(:math:`a=1`) :

.. math::
   \rho_{\Lambda 0}
   \;=\;
   \frac{\eta}{3}\int_{a_\star}^{1} \rho_\gamma(a')\, d(a'^3),
   \qquad d(a'^3)=3a'^2\,da'. \tag{C}

Cette relation est **toujours vraie**, indépendamment du détail de :math:`\rho_\gamma(a')`
(il suffit d’utiliser la bonne loi de :math:`\rho_\gamma` sous l’intégrale).

Deux voies de calcul
-----------------------

Approximation « ordre 1 » (η petit, faible rétro-action).
*********************************************************

On néglige l’effet du transfert sur :math:`\rho_\gamma` et l’on utilise
:math:`\rho_\gamma(a)=\rho_{r0}a^{-4}` dans (C) :

.. math::
   \rho_{\Lambda 0}
   \;=\;
   \frac{\eta}{3}\,\rho_{r0}\int_{a_\star}^{1} a^{-4}\, d(a^3)
   \;=\;
   \eta\,\rho_{r0}\int_{a_\star}^{1} a^{-2}\,da
   \;=\;
   \eta\,\rho_{r0}\,\big[-a^{-1}\big]_{a_\star}^{1}
   \;=\;
   \eta\,\rho_{r0}\,(a_\star^{-1}-1).

Avec :math:`a_\star^{-1}=1+z_\star` :

.. math::
   \rho_{\Lambda 0} \simeq \eta\,\rho_{r0}\,z_\star,
   \qquad
   \Omega_{\Lambda 0} \simeq \eta\,\Omega_{r0}\,z_\star. \tag{D}

C’est la **loi linéaire en** :math:`z_\star` utilisée comme estimateur d’ordre de grandeur.

Traitement auto-consistant (η constant).
****************************************

On résout le système couplé (B) :

.. math::
   \dot\rho_\gamma + (4+\eta)H\rho_\gamma = 0
   \;\Rightarrow\;
   \rho_\gamma(a) = \rho_{r0}\,a^{-(4+\eta)}.

Puis

.. math::
   \frac{d\rho_\Lambda}{d\ln a} = \eta\,\rho_\gamma
   \;\Rightarrow\;
   \rho_\Lambda(a)
   =
   \frac{\eta}{4+\eta}\,\rho_{r0}\,
   \big(a_\star^{-(4+\eta)} - a^{-(4+\eta)}\big).

Aujourd’hui (:math:`a=1`) :

.. math::
   \rho_{\Lambda 0}
   =
   \frac{\eta}{4+\eta}\,\rho_{r0}\,
   \big(a_\star^{-(4+\eta)} - 1\big)
   =
   \frac{\eta}{4+\eta}\,\big(\rho_\gamma(z_\star)-\rho_{r0}\big). \tag{E}

**Remarques.**

- Pour :math:`\eta\ll 1`, (E) ne se réduit **pas** à (D) mais indique un
  transfert proportionnel à la **densité passée du rayonnement**,
  :math:`\rho_\gamma(z_\star)\propto (1+z_\star)^4`, souvent trop grand si
  le processus démarre très tôt.  
- En pratique, (D) est l’approximation **« Born »** : rétro-action
  négligeable pendant l’intégration, utile pour cadrer les ordres de grandeur
  et guider le design d’:math:`\eta(a)`.

Généralisation : efficacité dépendant du temps
-------------------------------------------------

Pour un rendement **variable** :math:`\eta(a)` (fenêtre tardive, pic, etc.) :

.. math::
   \rho_{\Lambda 0}
   =
   \int_{\ln a_\star}^{0} \eta(a)\,\rho_\gamma(a)\, d\ln a. \tag{F}

- Si l’on garde la loi **non couplée** :math:`\rho_\gamma(a)=\rho_{r0}a^{-4}`,
  (F) donne immédiatement des formes analytiques simples selon le choix de
  :math:`\eta(a)` (ex. fenêtre tardive centrée à :math:`a\sim 0.5`).
- Pour un traitement **auto-consistant**, on résout d’abord
  :math:`d\rho_\gamma/d\ln a = -(4+\eta(a))\rho_\gamma`, puis on injecte
  dans (F).

Conditions de validité & lecture physique
--------------------------------------------

.. note::
   - (D) est valable si :math:`\eta` est **petit** et/ou actif **tard**,
     de sorte que l’impact sur :math:`\rho_\gamma` reste négligeable pendant
     l’intégration.  
   - (E) montre qu’un **η constant** actif **très tôt** sur-transfère
     (car :math:`\rho_\gamma(z)` croît comme :math:`(1+z)^4`). Cela impose
     soit :math:`\eta\ll 1`, soit une **fenêtre tardive** :math:`\eta(a)`
     (processus enclenché après recombinaison), pour rester compatible BBN/CMB.  
   - La formulation « travail comobile » (A) est **équivalente** à l’écriture
     « source » (B) avec :math:`Q=\eta H\rho_\gamma` : c’est simplement la
     puissance :math:`p\,\dot V / V = 3Hp` par unité de volume.

Passage aux densités réduites
--------------------------------

En divisant par :math:`\rho_{c0}` :

.. math::
   \Omega_{\Lambda 0}
   =
   \frac{\rho_{\Lambda 0}}{\rho_{c0}}
   \simeq
   \eta\,\Omega_{r0}\,z_\star \quad (\text{approx. (D)}),
   \qquad \text{ou} \qquad
   \Omega_{\Lambda 0}
   =
   \frac{\eta}{4+\eta}\,
   \frac{\rho_\gamma(z_\star)-\rho_{r0}}{\rho_{c0}}
   \quad (\text{exact (E)}).
