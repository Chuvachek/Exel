Here is the VBA code for the change log in TK-expertise


Sub FilterB_FromClipboard()
    Dim filterValue As String
    Dim lastRow As Long
    
    ' 1. Áåðåì òåêñò èç áóôåðà
    On Error Resume Next
    filterValue = CreateObject("htmlfile").parentWindow.clipboardData.GetData("text")
    On Error GoTo 0
    
    ' 2. Î÷èñòêà çíà÷åíèÿ
    filterValue = Trim(filterValue)
    filterValue = Replace(filterValue, Chr(10), "")
    filterValue = Replace(filterValue, Chr(13), "")
    
    ' Ïðîâåðêà: åñëè â áóôåðå íè÷åãî íåò
    If filterValue = "" Then
        MsgBox "Áóôåð îáìåíà ïóñò èëè ñîäåðæèò íå òåêñò", vbExclamation
        Exit Sub
    End If
    
    With ActiveSheet
        ' Ñ÷èòàåì ïîñëåäíþþ ñòðîêó
        lastRow = .Cells(.Rows.Count, "B").End(xlUp).Row
        If lastRow < 6 Then lastRow = 6
        
        ' Ñáðàñûâàåì ôèëüòð
        If .AutoFilterMode Then .AutoFilterMode = False
        
        ' ÏÐÈÌÅÍßÅÌ ÔÈËÜÒÐ ÑÎ ÇÂ¨ÇÄÎ×ÊÀÌÈ (ïîèñê ïî ÷àñòè òåêñòà)
        .Range("A6:B" & lastRow).AutoFilter _
            Field:=2, _
            Criteria1:="*" & filterValue & "*"
    End With
End Sub
Sub FilterG_ByNumber()
    Dim filterValue As String
    Dim lastRow As Long
    
    ' Çàïðàøèâàåì íîìåð ó ïîëüçîâàòåëÿ
    filterValue = InputBox("Ââåäèòå íîìåð äëÿ ïîèñêà â ñòîëáöå G:", "Ïîèñê ïî íîìåðó")
    
    ' Åñëè ïîëüçîâàòåëü íàæàë Îòìåíà èëè íè÷åãî íå ââ¸ë
    If filterValue = "" Then
        MsgBox "Ïîèñê îòìåí¸í", vbInformation
        Exit Sub
    End If
    
    ' Óáèðàåì ëèøíèå ïðîáåëû
    filterValue = Trim(filterValue)
    
    With ActiveSheet
        ' Íàõîäèì ïîñëåäíþþ ñòðîêó â ñòîëáöå G
        lastRow = .Cells(.Rows.Count, "G").End(xlUp).Row
        
        ' Ñáðàñûâàåì ôèëüòð
        If .AutoFilterMode Then .AutoFilterMode = False
        
        ' Ïðèìåíÿåì ôèëüòð ñ çâ¸çäî÷êàìè (èùåì ïî ÷àñòè òåêñòà)
        ' Íàïðèìåð, "12305" íàéä¸ò "VLS-TQ-(P0-75-011)-N-2715-12305-00"
        .Range("A6:G" & lastRow).AutoFilter _
            Field:=7, _
            Criteria1:="*" & filterValue & "*"
    End With
End Sub

Sub ResetFilter()
    With ActiveSheet
        If .FilterMode Then
            .ShowAllData
        End If
    End With
End Sub

Sub FilterG_FromClipboard()
    Dim filterValue As String
    Dim lastRow As Long
    
    filterValue = CreateObject("htmlfile").parentWindow.clipboardData.GetData("text")
    
    With ActiveSheet
        lastRow = .Cells(.Rows.Count, "G").End(xlUp).Row
        
        If .AutoFilterMode Then .AutoFilterMode = False
        
        .Range("A6:G" & lastRow).AutoFilter _
            Field:=7, _
            Criteria1:=filterValue
    End With
End Sub

Sub PasteCleanValues_Left()
    Dim rng As Range
    
    On Error GoTo ErrHandler

    ActiveSheet.Paste
    Set rng = Selection

    rng.ClearFormats

    With rng
        .HorizontalAlignment = xlLeft
        .VerticalAlignment = xlCenter
        .Font.Name = "Times New Roman"
        .Font.Size = 11
    End With

    With rng.Borders
        .LineStyle = xlContinuous
        .Weight = xlThin
    End With

    Application.CutCopyMode = False
    Exit Sub

ErrHandler:
    Application.StatusBar = "Paste error"
    Err.Clear
End Sub

Sub PasteCleanValues()
    Dim rng As Range
    
    On Error GoTo ErrHandler

    ActiveSheet.Paste
    Set rng = Selection

    rng.ClearFormats

    With rng
        .HorizontalAlignment = xlCenter
        .VerticalAlignment = xlCenter
        .Font.Name = "Times New Roman"
        .Font.Size = 11
    End With

    With rng.Borders
        .LineStyle = xlContinuous
        .Weight = xlThin
    End With

    Application.CutCopyMode = False
    Exit Sub

ErrHandler:
    Application.StatusBar = "Paste error"
    Err.Clear
End Sub

