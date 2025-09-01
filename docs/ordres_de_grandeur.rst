=================
Ordres de grandeur
=================

Point de départ (rayonnement aujourd’hui) :

.. math::
   \Omega_{r0} = \Omega_{\gamma0}\,[1+0.2271\,N_{\rm eff}], \qquad
   \Omega_{\gamma0} \simeq \frac{2.469\times 10^{-5}}{h^2} \quad (T_{\rm CMB}=2.7255~\mathrm{K}).

Exemple numérique (:math:`h=0.68`, :math:`N_{\rm eff}=3.044`) :

.. math::
   \Omega_{r0} \simeq 9.03\times 10^{-5}.

Avec l’estimateur linéaire déduit de la section précédente,

.. math::
   \Omega_{\Lambda 0} \simeq \eta\,\Omega_{r0}\, z_\star,

on obtient l’efficacité requise :

.. math::
   \eta \simeq \frac{\Omega_{\Lambda 0}}{\Omega_{r0}\, z_\star}.
   \qquad (\Omega_{\Lambda 0}\simeq 0.69)

.. list-table:: Quelques cas simples
   :header-rows: 1

   * - :math:`z_\star`
     - :math:`\eta` requis
   * - Recombinaison : :math:`\sim 1100`
     - :math:`\eta \approx 6.95`
   * - Égalité matière/rayonnement : :math:`\sim 3400`
     - :math:`\eta \approx 2.25`

.. note::
   **Lecture rapide.** Un \ :math:`\eta` d’ordre unité–quelques suffit
   si le processus démarre vers :math:`z_\star\sim 10^3`. Plus le démarrage est
   tardif (petit :math:`z_\star`), plus il faut un :math:`\eta` grand pour
   atteindre :math:`\Omega_{\Lambda0}`.

.. warning::
   **Domaine de validité.** 

   Ces estimations utilisent l’**estimateur linéaire**
   (rétro-action négligée sur :math:`\rho_\gamma`). Si :math:`\eta` est constant et
   actif très tôt, la solution auto-consistante montre un transfert proportionnel à
   :math:`\rho_\gamma(z_\star)\propto (1+z_\star)^4`, potentiellement en tension
   avec BBN/CMB.  
   
   Deux voies sûres :
      - **fenêtre tardive** : \ :math:`\eta(a)` activée autour de :math:`z\sim 10^3`
        avec amplitude modérée ; 
      -  *pondération comobile** (p. ex. \ :math:`\eta(a)\propto a^3`)
         comme dans notre hypothèse, qui mène naturellement à la loi linéaire en
         :math:`z_\star`.

.. tip::
   **À tester numériquement.** Implémenter \ :math:`Q(a)=\eta(a)\,H\,\rho_\gamma(a)`
   dans CLASS et scanner des fenêtres \ :math:`\eta(a)` (pic tardif, lois en
   :math:`a^n`, coupure avant recombinaison) pour confronter à CMB (N_eff, queue
   de Silk), SN/BAO/H(z), RSD et :math:`\sigma_8`.
