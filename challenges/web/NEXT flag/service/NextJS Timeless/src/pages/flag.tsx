// flag.tsx
import { useEffect, useState } from 'react';
import { useRouter } from 'next/router';
import { parseCookies, setCookie, destroyCookie } from 'nookies'

const FlagPage = () => {
    const router = useRouter();
    const [showFlag, setShowFlag] = useState<boolean>(false);
    const [flag, setFlag] = useState<string>('');

    useEffect(() => {
        const session = parseCookies().session;

        if (session === 'ca65fb7e5a62cc4133ea9cb3a486f910') {
            // Session is valid; show flag
            setShowFlag(true);

            //get request from /api/flag for flag
            fetch('/api/flag')
                .then((res) => res.json())
                .then((data) => {
                    setFlag(data.flag);
                });
                
        } else {
            // Redirect to login page
            destroyCookie(null, 'session');
            router.push('/');
        }
    }, [router]);

    return (
        <>
            {showFlag && <div>{flag}</div>}
        </>
    );
};

export default FlagPage;
