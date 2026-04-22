
;; Inhibir pantalla de incio
(setq inhibit-startup-screen t)

;; Permite usar solo 'y' en lugar de 'yes'.
(setq use-short-answers t)

;; Asegurarse de que agregue parentesis cerrando
(electric-pair-mode 1) ()

;; Llenar texto hasta 80 caracteres
(setq fill-column 80)

;; Esconder toolbar, scrollbar y menu
(tool-bar-mode -1)
(scroll-bar-mode -1)
(menu-bar-mode -1)

;; Permite remover area seleccionada al teclear nuevo texto
(delete-selection-mode t)

;; Permite ver numero de columna en modeline
(global-display-line-numbers-mode 1)
(setq column-number-mode t)

;; Resalta parentesis pareja
;; (show-paren-mode 1)

;; Como mostrar parentesis pareja cuando esta fuera de pantalla
(setq show-paren-context-when-offscreen 'overlay)

;; Usar tab para completar
(setq tab-always-indent 'complete)

;; Paquetes

(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

;;Ewal para colores

(use-package ewal
  :init (setq ewal-use-built-in-always-p nil
              ewal-use-built-in-on-failure-p t
              ewal-built-in-palette "sexy-material"))
(use-package ewal-spacemacs-themes
  :init (progn
          (setq spacemacs-theme-underline-parens t
                my:rice:font (font-spec
                              :family "Space Mono Nerd Font"
                              :weight 'regular
                              :size 14.0))
          (show-paren-mode +1)
          (global-hl-line-mode)
          (set-frame-font my:rice:font nil t)
          (add-to-list  'default-frame-alist
                        `(font . ,(font-xlfd-name my:rice:font))))
  :config (progn
            (load-theme 'ewal-spacemacs-modern t)
            (enable-theme 'ewal-spacemacs-modern)))
(use-package ewal-evil-cursors
  :after (ewal-spacemacs-themes)
  :config (ewal-evil-cursors-get-colors
           :apply t :spaceline t))
(use-package spaceline
  :after (ewal-evil-cursors winum)
  :init (setq powerline-default-separator nil)
  :config (spaceline-spacemacs-theme))
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages
   '(ewal-doom-themes ewal-evil-cursors ewal-spacemacs-themes treemacs)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

;; Transparencia
(add-to-list 'default-frame-alist '(alpha-background . 90)) ; 90% opaco


