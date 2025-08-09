# File Preparation Script
# Run directly from terminal or with PowerShell

function Prepare-Files {
    param(
        [Parameter(Mandatory=$false)]
        [string[]]$Files = $null
    )

    # If no files specified, get all files in the project
    if ($null -eq $Files) {
        $Files = Get-ChildItem -Recurse -Include *.rb, *.py, *.js, *.ts, *.cs, *.java, *.go, *.md -File | Resolve-Path -Relative
    }

    # Prepare the output string
    $output = "Included Files`n`n"
    $output += ($Files | ForEach-Object { "* $_" }) -join "`n"
    $output += "`n`nSource:`n`n"

    # Add content for each file
    foreach ($file in $Files) {
        $output += "``$file``:`n`n"
        $output += "``````"
        $output += Get-Content $file -Raw
        $output += "``````"
        $output += "`n`n"
    }

    # Copy to clipboard
    $output.Trim() | Set-Clipboard
    Write-Host "Output copied to clipboard"
}

# If script is run directly with no arguments, prepare all files
if ($MyInvocation.UnboundArguments.Count -eq 0) {
    Prepare-Files
}
# If arguments are provided, prepare specific files
else {
    Prepare-Files -Files $MyInvocation.UnboundArguments
}