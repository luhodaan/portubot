/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext } from "react"
import { Box as RadixThemesBox, Button as RadixThemesButton, Flex as RadixThemesFlex, Text as RadixThemesText, TextField as RadixThemesTextField } from "@radix-ui/themes"
import { EventLoopContext, StateContexts } from "$/utils/context"
import { DebounceInput } from "react-debounce-input"
import { Event, isNotNullOrUndefined } from "$/utils/state"
import NextHead from "next/head"



export function Box_e1a9ab2ef92d1df26e29526f256384b8 () {
  
  const reflex___state____state__portubot___state____state = useContext(StateContexts.reflex___state____state__portubot___state____state)





  
  return (
    <RadixThemesBox>

<>{ reflex___state____state__portubot___state____state.chat_history.map((messages, index_6f76867f8a25674e) => (
  <RadixThemesBox css={({ ["marginTop"] : "1em", ["marginBottom"] : "1em", ["width"] : "100%" })} key={index_6f76867f8a25674e}>

<RadixThemesBox css={({ ["textAlign"] : "right" })}>

<RadixThemesText as={"p"} css={({ ["padding"] : "1em", ["borderRadius"] : "8px", ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em", ["boxShadow"] : "rgba(0, 0, 0, 0.15) 0px 2px 8px", ["maxWidth"] : "30em", ["display"] : "inline-block", ["color"] : "#FFFFFF", ["marginLeft"] : "20%", ["backgroundColor"] : "#009739", ["borderLeft"] : "4px solid #FEDD00" })}>

{messages.at(0)}
</RadixThemesText>
</RadixThemesBox>
<RadixThemesBox css={({ ["textAlign"] : "left" })}>

<RadixThemesText as={"p"} css={({ ["padding"] : "1em", ["borderRadius"] : "8px", ["marginTop"] : "0.5em", ["marginBottom"] : "0.5em", ["boxShadow"] : "rgba(0, 0, 0, 0.15) 0px 2px 8px", ["maxWidth"] : "30em", ["display"] : "inline-block", ["color"] : "#012169", ["marginRight"] : "20%", ["backgroundColor"] : "#FEDD00", ["borderRight"] : "4px solid #009739" })}>

{messages.at(1)}
</RadixThemesText>
</RadixThemesBox>
</RadixThemesBox>
))}</>
</RadixThemesBox>
  )
}

export function Button_12e0ef099b07ec3906330941ebd1f0cc () {
  
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_click_81d21bbe77ae3ec12fbc0c929c4eac57 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.portubot___state____state.answer", ({  }), ({  })))], args, ({  })))), [addEvents, Event])



  
  return (
    <RadixThemesButton css={({ ["backgroundColor"] : "#012169", ["color"] : "#FFFFFF", ["boxShadow"] : "rgba(0, 0, 0, 0.15) 0px 2px 8px", ["borderRadius"] : "20px", ["padding"] : "0.7em 1.5em", ["&:hover"] : ({ ["backgroundColor"] : "#3B7A57", ["transform"] : "scale(1.05)" }), ["transition"] : "all 0.3s ease" })} onClick={on_click_81d21bbe77ae3ec12fbc0c929c4eac57}>

{"Ask"}
</RadixThemesButton>
  )
}

export function Debounceinput_408ee9d1a997c7ea20effa06b474c95e () {
  
  const reflex___state____state__portubot___state____state = useContext(StateContexts.reflex___state____state__portubot___state____state)
  const [addEvents, connectErrors] = useContext(EventLoopContext);


  const on_change_8b8bea9c515a06bcac5046c69eb21abf = useCallback(((_e) => (addEvents([(Event("reflex___state____state.portubot___state____state.set_question", ({ ["value"] : _e["target"]["value"] }), ({  })))], [_e], ({  })))), [addEvents, Event])



  
  return (
    <DebounceInput css={({ ["borderWidth"] : "1px", ["borderColor"] : "#009739", ["padding"] : "0.7em", ["boxShadow"] : "rgba(0, 0, 0, 0.15) 0px 2px 8px", ["width"] : "350px", ["borderRadius"] : "20px", ["&:focus"] : ({ ["borderColor"] : "#012169" }) })} debounceTimeout={300} element={RadixThemesTextField.Root} onChange={on_change_8b8bea9c515a06bcac5046c69eb21abf} placeholder={"Ask a question"} value={(isNotNullOrUndefined(reflex___state____state__portubot___state____state.question) ? reflex___state____state__portubot___state____state.question : "")}/>
  )
}

export default function Component() {
    




  return (
    <Fragment>

<RadixThemesFlex css={({ ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" })}>

<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<Box_e1a9ab2ef92d1df26e29526f256384b8/>
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} gap={"3"}>

<Debounceinput_408ee9d1a997c7ea20effa06b474c95e/>
<Button_12e0ef099b07ec3906330941ebd1f0cc/>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesFlex>
<NextHead>

<title>

{"Portubot | Index"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</Fragment>
  )
}
