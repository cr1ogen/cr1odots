(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
;; Comment/uncomment this line to enable MELPA Stable if desired.  See `package-archive-priorities`
;; and `package-pinned-packages`. Most users will not need or want to do this.
;;(add-to-list 'package-archives '("melpa-stable" . "https://stable.melpa.org/packages/") t)
(package-initialize)

(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

(use-package which-key
  :ensure t
  :config (which-key-mode)) 
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-safe-themes
   '("7e377879cbd60c66b88e51fad480b3ab18d60847f31c435f15f5df18bdb18184" "da75eceab6bea9298e04ce5b4b07349f8c02da305734f7c0c8c6af7b5eaa9738" "88f7ee5594021c60a4a6a1c275614103de8c1435d6d08cc58882f920e0cec65e" default))
 '(package-selected-packages
   '(ewal-spacemacs-themes ewal-evil-cursors ewal neotree treemacs-projectile treemacs tremacs dashboard helm-projectile projectile helm all-the-icons doom-modeline which-key)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(add-to-list 'default-frame-alist
                  '(font . "Monospace-12"))

;;(use-package doom-themes
;;  :ensure t
;; :config
;;  (load-theme 'doom-one))

(use-package doom-modeline
  :ensure t
  :hook (after-init . doom-modeline-mode))

(use-package all-the-icons
  :ensure t)

;; No startup message
(setq inhibit-startup-message t)

;; No mostrar barra de herramientas
(tool-bar-mode -1)


;; No mostrar menu
(menu-bar-mode -1)

;; Resaltar linea
(global-hl-line-mode +1)

;; Borrar seleccion
(delete-selection-mode 1)

;; Mostrar numero de linea
(add-hook 'prog-mode-hook 'display-line-numbers-mode)

;; Mostrar parentesis
(show-paren-mode 1)

(use-package projectile
  :ensure t
  :config
  (define-key projectile-mode-map (kbd "C-c p") 'projectile-command-map)
  (projectile-mode +1))

(use-package dashboard
  :ensure t
  :init
  (progn
    (setq dashboard-items '((recents . 1)
			    (projects . 1))))
    (setq dashboard-show-shortcuts nil)
    (setq dashboard-center-content nil)
    (setq dashboard-banner-logo-tile "DEBIAN EMACS RULES")
    (setq dashboard-icon-type 'all-the-icons) 
    (setq dashboard-set-file-icons t)
    (setq dashboard-set-heading-icons t)
    (setq dashboard-startup-banner "~/Imágenes/pinguino.png")
    (setq dashboard-set-navigator t)
    )


  
  :config
(dashboard-setup-startup-hook)

(use-package treemacs
  :ensure t
  :bind
  (:map global-map
	([f8] . treemacs))
        ("C-<f8>" . treemacs-select-window))
  :config
  (setq treemacs-is-never-other-window t)

(use-package treemacs-projectile
  :after treemacs projectile
  :ensure t)

;; opacity
(add-to-list 'default-frame-alist '(alpha-background . 90))


(use-package ewal
  :init (setq ewal-use-built-in-always-p nil
              ewal-use-built-in-on-failure-p t
              ewal-built-in-palette "sexy-material"))
(use-package ewal-spacemacs-themes
  :init (progn
          (setq spacemacs-theme-underline-parens t
                my:rice:font (font-spec
                              :family "Mononoki Nerd Font"
                              :weight 'semi-bold
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


