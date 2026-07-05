import QtQuick
import QtQuick.Controls
import Quickshell
import Quickshell.Wayland

ShellRoot {
    id: root

    Loader {
        id: themeLoader
        source: "Appearance.colors.qml"
    }

    readonly property var theme: themeLoader.item ? themeLoader.item : null
    
    property color colorFondo:      theme ? theme.colorFondo      : "#1e1e2e"
    property color colorBorde:      theme ? theme.colorBorde      : "#89b4fa"
    property color colorHoyFondo:   theme ? theme.colorHoyFondo   : "#89b4fa"
    property color colorHoyTexto:   theme ? theme.colorHoyTexto   : "#11111b"
    property color colorMesActual:  theme ? theme.colorMesActual  : "#cdd6f4"
    property color colorMesFuera:   theme ? theme.colorMesFuera   : "#585b70"
    property color colorDiasSemana: theme ? theme.colorDiasSemana : "#f5c2e7"

    PanelWindow {
        id: window
        visible: true
        
        // Aumenté el tamaño general de la ventana para que entre el texto más grande
        width: 380
        height: 400

        WlrLayershell.layer: WlrLayer.Top
        WlrLayershell.namespace: "calendar_popup"
        WlrLayershell.keyboardFocus: WlrKeyboardFocus.Exclusive

        anchors {
            top: true
            right: true
        }

        margins {
            top: 56
            right: 16
        }

        Rectangle {
            anchors.fill: parent
            color: root.colorFondo
            border.color: root.colorBorde
            
            // BORDES MÁS GRANDES: Aumenté el grosor del contorno y el radio de las esquinas
            border.width: 6 
            radius: 0

            Button {
                id: closeButton
                text: "✕"
                anchors.top: parent.top
                anchors.right: parent.right
                anchors.margins: 12
                width: 28
                height: 28
                onClicked: Qt.quit()
                
                background: Rectangle {
                    color: closeButton.hovered ? root.colorHoyFondo : "transparent"
                    radius: 6
                }
                contentItem: Text {
                    text: closeButton.text
                    font.bold: true
                    font.pointSize: 12 // Letra del botón de cierre un poco más grande
                    color: closeButton.hovered ? root.colorHoyTexto : root.colorMesFuera
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
            }

            Column {
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 20
                spacing: 10 

                // FILA DE DÍAS DE LA SEMANA (Lu, Ma, Mi...)
                DayOfWeekRow {
                    width: 340 // Más ancho para dar espacio
                    locale: Qt.locale("es_AR")
                    
                    delegate: Text {
                        text: model.shortName
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.bold: true
                        
                        // LETRAS MÁS GRANDES: Aumenté el tamaño de la fuente
                        font.pointSize: 13 
                        color: root.colorDiasSemana
                    }
                }

                // GRILLA NUMÉRICA DEL MES
                MonthGrid {
                    id: grid
                    width: 340
                    height: 280 // Más alto para los números grandes
                    month: new Date().getMonth()
                    year: new Date().getFullYear()
                    locale: Qt.locale("es_AR")

                    delegate: Rectangle {
                        // Casilleros individuales más grandes para que no se peguen los números
                        implicitWidth: 48
                        implicitHeight: 48
                        color: model.today ? root.colorHoyFondo : "transparent"
                        radius: 6 // Bordes individuales internos levemente más marcados

                        Text {
                            anchors.centerIn: parent
                            text: model.day
                            font.bold: model.today
                            
                            // NÚMEROS MÁS GRANDES: Pasaron de tamaño por defecto a 14
                            font.pointSize: 14 
                            color: model.today ? root.colorHoyTexto : (model.month === grid.month ? root.colorMesActual : root.colorMesFuera)
                        }
                    }
                }
            }
        }
    }
}
